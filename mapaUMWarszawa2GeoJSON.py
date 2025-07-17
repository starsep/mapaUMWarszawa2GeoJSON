#!/usr/bin/env python3
import geojson
from geojson import Feature, Point, FeatureCollection
from hashlib import md5
from typing import Tuple, List, Dict

import overpy
from tqdm import tqdm

import json
import re
from pathlib import Path

import httpx
from pyproj import Transformer, CRS
from pyproj import Geod

DEFAULT_TAG = ("amenity", "restaurant")
DISTANCE_THRESHOLD = 100.0


httpxClient = httpx.Client(timeout=None)


class MapaUMWarszawa2GeoJSON:
    def __init__(self, cacheEnabled=True):
        self.wgs84Geod = Geod(ellps="WGS84")
        self.transformer = Transformer.from_crs(CRS("epsg:2178"), "wgs84")
        self.cacheEnabled = cacheEnabled
        self.overpassApi = overpy.Overpass()

    @staticmethod
    def addQuotesToJSONKeys(data: str) -> str:
        r = re.compile(r"(?P<separator>[{,])(?P<key>[a-zA-Z]+):")
        return r.sub(r'\g<separator>"\g<key>":', data)

    @staticmethod
    def parseTagsFromName(name: str) -> Dict[str, str]:
        def handleMultilineNames(lines: List[str]) -> List[str]:
            result = []
            partialResult = None
            for line in lines:
                if ": " in line:
                    if partialResult is not None:
                        result.append(partialResult)
                    partialResult = line
                else:
                    if partialResult is None:
                        raise ValueError(f"Unexpected input: {lines}")
                    partialResult += "\n" + line
            if partialResult is not None:
                result.append(partialResult)
            return result

        return {
            k: v
            for k, v in map(
                lambda x: x.split(": ")[:2], handleMultilineNames(name.split("\n"))
            )
            if v != ""
        }

    @staticmethod
    def downloadData(theme: str) -> str:
        return httpxClient.post(
            "https://mapa.um.warszawa.pl/mapviewer/foi",
            params=dict(
                request="getfoi",
                version="1.0",
                bbox="0:1787369:9500502:9791137",
                width=760,
                height=1190,
                theme=theme,
                dstsrid=2178,
                cachefoi="yes",
                tid="85_311281927602616807",
                aw="no",
            ),
        ).text

    def downloadDataWithCache(self, theme: str) -> FeatureCollection:
        umDataDir = Path("umRawData")
        umDataDir.mkdir(exist_ok=True)
        umDataPath = umDataDir / (theme + ".raw")
        if not umDataPath.exists() or not self.cacheEnabled:
            umDataPath.write_text(self.downloadData(theme))
        umData = json.loads(self.addQuotesToJSONKeys(umDataPath.read_text()))[
            "foiarray"
        ]
        features = []

        for point in umData:
            tags = self.parseTagsFromName(point["name"])
            lat, lng = self.transformer.transform(point["y"], point["x"])
            features.append(Feature(geometry=Point((lng, lat)), properties=tags))
        return FeatureCollection(features)

    @staticmethod
    def elementQuery(overpassQuery: List[Tuple[str, str]]):
        return "".join([f'["{tag}"="{value}"]' for (tag, value) in overpassQuery])

    def downloadOverpassData(
        self, overpassQuery: List[Tuple[str, str]]
    ) -> FeatureCollection:
        overpassDir = Path("overpass")
        overpassDir.mkdir(exist_ok=True)
        elementQuery = self.elementQuery(overpassQuery)
        query = f"""
            area["name"="Warszawa"]["admin_level"=6];
            (
                nwr{elementQuery}(area);
            );
            out center;
        """
        queryHash = md5(bytes(query, "utf-8")).hexdigest()
        overpassOutputPath = overpassDir / (queryHash + ".geojson")
        if not overpassOutputPath.exists() or not self.cacheEnabled:
            overpassResult = self.overpassApi.query(query)
            features = []
            for node in overpassResult.nodes:
                features.append(
                    Feature(geometry=Point((float(node.lon), float(node.lat))))
                )
            for way in overpassResult.ways:
                features.append(
                    Feature(
                        geometry=Point((float(way.center_lon), float(way.center_lat)))
                    )
                )
            geojson.dump(FeatureCollection(features), overpassOutputPath.open("w"))
        return geojson.load(overpassOutputPath.open("r"))

    def removeLikelyDuplicates(
        self, overpassData: FeatureCollection, umData: FeatureCollection
    ) -> FeatureCollection:
        features = []
        for umPoint in umData["features"]:
            umLat, umLng = umPoint["geometry"]["coordinates"]
            minDistance = DISTANCE_THRESHOLD + 1
            for osmPoint in overpassData["features"]:
                osmLat, osmLng = osmPoint["geometry"]["coordinates"]
                minDistance = min(
                    minDistance, self.wgs84Geod.inv(umLng, umLat, osmLng, osmLat)[2]
                )
                if minDistance <= DISTANCE_THRESHOLD:
                    break
            if minDistance > DISTANCE_THRESHOLD:
                features.append(umPoint)
        return FeatureCollection(features)

    def process(self, theme: str, overpassQuery: List[Tuple[str, str]]):
        outputData = self.downloadDataWithCache(theme)
        if len(overpassQuery) > 0:
            overpassData = self.downloadOverpassData(overpassQuery=overpassQuery)
            deduplicatedData = self.removeLikelyDuplicates(
                overpassData=overpassData, umData=outputData
            )
            outputData = deduplicatedData
        writeOutput(theme=theme, data=outputData)


def writeOutput(theme: str, data: FeatureCollection):
    outputDir = Path("output")
    outputDir.mkdir(exist_ok=True)
    outputPath = outputDir / (theme + ".geojson")
    geojson.dump(data, outputPath.open("w"))


def main():
    SPORT_ATHLETICS = ("sport", "athletics")
    SPORT_UNKNOWN = ("sport", "fake")
    FITNESS_CENTRE = ("leisure", "fitness_centre")
    dataSets: List[Tuple[str, str]] = [
        ("dane_wawa.I_TOALETY", [("amenity", "toilets")]),
        ("dane_wawa.BOS_ZIELEN_POMNIKI_SM_NEW", [("denotation", "natural_monument")]),
        ("dane_wawa.BOS_ZIELEN_POMNIKI_NEW", [("denotation", "natural_monument")]),
        ("dane_wawa.ZEZWOLENIA_ALKOHOLOWE_GASTRO", []),
        ("dane_wawa.ZEZWOLENIA_ALKOHOLOWE_GASTRO_A", []),
        ("dane_wawa.ZEZWOLENIA_ALKOHOLOWE_DETAL", []),
        ("dane_wawa.ZEZWOLENIA_ALKOHOLOWE_DETAL_A", []),
        ("dane_wawa.KU_POMNIKI", []),
        ("dane_wawa.KU_TABLICE", []),
        (
            "dane_wawa.K_ZTM_BILETOMATY_STACJONARNE",
            [("vending", "public_transport_tickets")],
        ),
        # Rowery
        ("dane_wawa.ROWERY_STOJAKI_ROWEROWE", [("amenity", "bicycle_parking")]),
        # Place zabaw
        ("dane_wawa.I_PLACE_ZABAW_POINT", [("leisure", "playground")]),
        # Sport
        ("dane_wawa.S_BIEZNIE", [("leisure", "track")]),
        ("dane_wawa.S_FITNESS", [FITNESS_CENTRE]),
        ("dane_wawa.S_HALE_SPORTOWE", [("leisure", "sports_hall")]),
        ("dane_wawa.S_INNE", [SPORT_UNKNOWN]),
        ("dane_wawa.S_KORTY_TENISOWE", [("sport", "tennis")]),
        (
            "dane_wawa.S_KOSZYKOWKA",
            [("leisure", "pitch")],
        ),  # [("sport", "basketball")]),
        ("dane_wawa.S_KREGIELNIE", [("sport", "9pin")]),
        ("dane_wawa.S_LODOWISKA", [("sport", "ice_skating")]),
        ("dane_wawa.S_PCHNIECIE_KULA", [SPORT_UNKNOWN]),
        ("dane_wawa.S_PILKA_NOZNA", [("sport", "soccer")]),
        ("dane_wawa.S_PILKA_RECZNA", [("sport", "handball")]),
        ("dane_wawa.S_PLYWALNIE_KRYTE", [("leisure", "swimming_pool")]),
        ("dane_wawa.S_PLYWALNIE_ODKRYTE", [("leisure", "swimming_pool")]),
        ("dane_wawa.S_SALE_GIMNASTYCZNE", [("sport", "gymnastics")]),
        ("dane_wawa.S_SALE_I_PAWILONY", [SPORT_UNKNOWN]),
        ("dane_wawa.S_SCIANKI_WSPINACZKOWE", [("sport", "climbing")]),
        ("dane_wawa.S_SIATKOWKA", [("sport", "basketball")]),
        ("dane_wawa.S_SILOWNIE", [FITNESS_CENTRE]),
        ("dane_wawa.S_SILOWNIE_PLENEROWE", [FITNESS_CENTRE]),
        ("dane_wawa.S_SKATEPARKI", [("sport", "skateboard")]),
        ("dane_wawa.S_SKOKI_W_DAL", [SPORT_ATHLETICS]),
        ("dane_wawa.S_SKOKI_WZWYZ", [SPORT_ATHLETICS]),
        ("dane_wawa.S_SPORTY_LODZIOWE", [("sport", "sailing")]),
        ("dane_wawa.S_SQUASH", [("sport", "squash")]),
        ("dane_wawa.S_STADIONY_LA", [SPORT_ATHLETICS]),
        ("dane_wawa.S_STRZELNICE", [("sport", "shooting")]),
        ("dane_wawa.S_TORY", [SPORT_UNKNOWN]),
        # ("", [()]),
        # TODO: ("dane_wawa.I_UJECIA_WOD_PODZIEMNYCH", [()]),
    ]
    for theme, overpassQuery in tqdm(dataSets):
        MapaUMWarszawa2GeoJSON().process(theme=theme, overpassQuery=overpassQuery)


if __name__ == "__main__":
    main()
