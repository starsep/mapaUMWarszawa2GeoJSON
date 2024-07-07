#!/usr/bin/env python3
import asyncio
import itertools
import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

import geojson
import httpx
from jinja2 import Environment, FileSystemLoader, select_autoescape, StrictUndefined
from tqdm.asyncio import tqdm

from osmTags import osmTagsForTheme
from models import Theme, ThemeResult, ThemeCollectionResult
from themes import themes
from starsep_utils import (
    formatFileSize,
    GeoPoint,
    removeLikelyDuplicates,
    downloadOverpassData,
)

httpxClient = httpx.AsyncClient()

ghPagesDir = Path("gh-pages")
testMapDir = ghPagesDir / "testMap"
iconsDir = ghPagesDir / "icons"
deduplicatedDir = ghPagesDir / "deduplicated"


# TODO: move to starsep_utils?
def _bboxGeojsonGeometry(geometry: dict) -> tuple[GeoPoint, GeoPoint]:
    geometryType = geometry["type"]
    coordinates = geometry["coordinates"]
    match geometryType:
        case "MultiPolygon":
            bboxes = []
            for polygon in coordinates:
                polygonGeometry = dict(coordinates=polygon, type="Polygon")
                bboxes.append(_bboxGeojsonGeometry(polygonGeometry))
            return (
                GeoPoint(
                    lat=min([bbox[0].lat for bbox in bboxes]),
                    lon=min([bbox[0].lon for bbox in bboxes]),
                ),
                GeoPoint(
                    lat=max([bbox[1].lat for bbox in bboxes]),
                    lon=max([bbox[1].lon for bbox in bboxes]),
                ),
            )
        case "Polygon":
            minLat, maxLat, minLon, maxLon = (
                float("inf"),
                float("-inf"),
                float("inf"),
                float("-inf"),
            )
            for line in coordinates:
                for i in range(0, len(line), 2):
                    minLon = min(line[i], minLon)
                    maxLon = max(line[i], maxLon)
                    minLat = min(line[i + 1], minLat)
                    maxLat = max(line[i + 1], maxLat)
            return (
                GeoPoint(lat=minLat, lon=minLon),
                GeoPoint(lat=maxLat, lon=maxLon),
            )
        case "Point":
            point = GeoPoint(lat=coordinates[1], lon=coordinates[0])
            return point, point
        case t:
            raise Exception(f"Unsupported geometry type {t}")


@dataclass(frozen=True)
class FeatureWithCenter(GeoPoint):
    feature: dict


# TODO: move to starsep_utils?
def centerOfBboxGeojsonFeature(feature: dict) -> GeoPoint:
    minBbox, maxBbox = _bboxGeojsonGeometry(feature["geometry"])
    return GeoPoint(
        lat=(minBbox.lat + maxBbox.lat) / 2,
        lon=(minBbox.lon + maxBbox.lon) / 2,
    )


async def downloadDataTestMapa(theme: Theme):
    result = await httpxClient.post(
        "https://testmapa.um.warszawa.pl/mapviewer/dataserver/DANE_WAWA",
        headers={
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        },
        params=dict(
            t=theme.umKey,
            include_label_box="false",
            to_srid="4326",
            bbox_srid="4326",
        ),
    )
    result.raise_for_status()
    data = result.json()
    if "mds_error" in data:
        raise ValueError(data["mds_error"])
    for feature in data["features"]:
        if "_label_" in feature["properties"]:
            for tag in feature["properties"]["_label_"].split("\n"):
                split = tag.split(": ")
                if ": " not in tag or len(split) != 2:
                    continue
                key, value = split
                feature["properties"][key] = value
            del feature["properties"]["_label_"]
        if "styles" in feature:
            del feature["styles"]
    return data


def generateHTML(context: dict):
    env = Environment(
        loader=FileSystemLoader(searchpath="./templates"),
        autoescape=select_autoescape(),
        trim_blocks=True,
        lstrip_blocks=True,
        undefined=StrictUndefined,
    )
    template = env.get_template("index.j2")
    with (ghPagesDir / "index.html").open("w") as f:
        f.write(template.render(**context))


def processOverpassData(theme: Theme, data: dict, osmTags: list[list[str]]) -> str:
    outputFile = deduplicatedDir / (theme.umKey + ".geojson")
    if outputFile.exists():
        # TODO: remove this caching mechanism
        return formatFileSize(outputFile.stat().st_size)
    subqueries = "\n".join(
        [
            "nwr" + "".join([f"[{rule}]" for rule in rules]) + "(area);"
            for rules in osmTags
        ]
    )
    query = f"""
        area["name"="Warszawa"]["admin_level"=6];
        (
            {subqueries}
        );
        (._;>;);
        out;
    """
    overpassResult = downloadOverpassData(query=query)
    features: list[FeatureWithCenter] = []
    for feature in data["features"]:
        center = centerOfBboxGeojsonFeature(feature)
        features.append(
            FeatureWithCenter(
                feature=feature,
                lat=center.lat,
                lon=center.lon,
            )
        )
    result = removeLikelyDuplicates(100, features, overpassResult)
    with outputFile.open("w") as f:
        text = geojson.dumps(
            dict(features=[x.feature for x in result], type="FeatureCollection")
        )
        f.write(text)
    return formatFileSize(len(text))


async def processTheme(theme: Theme, themeCollectionName: str) -> ThemeResult | None:
    try:
        data = await downloadDataTestMapa(theme)
        outputFile = testMapDir / (theme.umKey + ".geojson")
        with outputFile.open("w") as f:
            text = geojson.dumps(data)
            f.write(text)
        osmTags = osmTagsForTheme[theme.umKey] if theme.umKey in osmTagsForTheme else []
        deduplicatedSize = None
        if len(osmTags) != 0:
            try:
                deduplicatedSize = processOverpassData(theme, data, osmTags)
            except Exception as e:
                logging.error(f"Failed to processOverpassData {theme.umKey}: {e}")
        return ThemeResult(
            theme=theme,
            size=formatFileSize(len(text)),
            themeCollectionName=themeCollectionName,
            osmTags=osmTags,
            deduplicatedSize=deduplicatedSize,
        )
    except Exception as e:
        logging.error(f"Failed to download {theme.umKey}: {e}")
        return None


async def downloadIcon(theme: Theme):
    iconPath = iconsDir / (theme.umKey + ".png")
    if iconPath.exists():
        return
    try:
        response = await httpxClient.get(theme.downloadIconUrl())
        response.raise_for_status()
        if "not found" in response.text:
            logging.error(f"Icon not found for {theme}")
            return
        with iconPath.open("wb") as f:
            f.write(response.content)
    except Exception as e:
        logging.error(f"Failed to download icon for {theme}: {e}")


async def downloadIcons():
    iconsDir.mkdir(exist_ok=True)
    await tqdm.gather(
        *[
            downloadIcon(theme)
            for themeCollection in themes
            for theme in themeCollection.themes
        ],
        desc="🖼️ Downloading icons",
    )


async def getThemesData() -> list[ThemeCollectionResult]:
    fetchedResults = await tqdm.gather(
        *[
            processTheme(theme, themeCollection.name)
            for themeCollection in themes
            for theme in themeCollection.themes
        ],
        desc="🗺️ Downloading map data",
    )
    return sorted(
        [
            ThemeCollectionResult(
                themeCollectionName=themeCollectionName,
                themes=sorted(
                    [
                        themeResult
                        for themeResult in themeResults
                        if themeResult is not None
                    ],
                    key=lambda themeResult: themeResult.theme.umKey,
                ),
            )
            for themeCollectionName, themeResults in itertools.groupby(
                fetchedResults, key=lambda themeResult: themeResult.themeCollectionName
            )
        ],
        key=lambda collection: collection.themeCollectionName,
    )


async def main():
    startTime = datetime.now()
    testMapDir.mkdir(exist_ok=True)
    deduplicatedDir.mkdir(exist_ok=True)
    processedThemes = await getThemesData()
    generateHTML(
        context=dict(
            generationSeconds=int((datetime.now() - startTime).total_seconds()),
            startTime=startTime.isoformat(timespec="seconds"),
            processedThemes=processedThemes,
        )
    )
    await downloadIcons()


if __name__ == "__main__":
    ghPagesDir.mkdir(exist_ok=True)
    asyncio.run(main())
