#!/usr/bin/env python3
import asyncio
import itertools
import logging
from datetime import datetime
from pathlib import Path

import geojson
import httpx
from jinja2 import Environment, FileSystemLoader, select_autoescape, StrictUndefined
from tqdm.asyncio import tqdm

from models import Theme, ThemeResult
from themes import themes
from utils import formatFileSize

httpxClient = httpx.AsyncClient()

ghPagesDir = Path("gh-pages")
testMapDir = ghPagesDir / "testMap"
iconsDir = ghPagesDir / "icons"


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


async def processTheme(theme: Theme, themeCollectionName: str) -> ThemeResult | None:
    try:
        data = await downloadDataTestMapa(theme)
        outputFile = testMapDir / (theme.umKey + ".geojson")
        with outputFile.open("w") as f:
            text = geojson.dumps(data)
            f.write(text)
            return ThemeResult(
                theme=theme,
                size=formatFileSize(len(text)),
                themeCollectionName=themeCollectionName,
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


async def getThemesData() -> list[list[ThemeResult]]:
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
            sorted(
                [
                    themeResult
                    for themeResult in themeResults
                    if themeResult is not None
                ],
                key=lambda themeResult: themeResult.theme.umKey,
            )
            for themeCollectionName, themeResults in itertools.groupby(
                fetchedResults, key=lambda themeResult: themeResult.themeCollectionName
            )
        ],
        key=lambda collection: collection[0].themeCollectionName,
    )


async def main():
    startTime = datetime.now()
    testMapDir.mkdir(exist_ok=True)
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
