#!/usr/bin/env python3
import csv
from hashlib import md5
from typing import Tuple, List

import overpass as overpass
import overpy
from tqdm import tqdm

import json
import re
from pathlib import Path

import requests
from pyproj import Transformer, CRS
from pyproj import Geod

DEFAULT_TAG = ("amenity", "restaurant")
DISTANCE_THRESHOLD = 100.0


class UMWarszawaToCSV:
    def __init__(self, cacheEnabled=True):
        self.wgs84Geod = Geod(ellps="WGS84")
        self.transformer = Transformer.from_crs(CRS("epsg:2178"), "wgs84")
        self.cacheEnabled = cacheEnabled
        self.overpassApi = overpy.Overpass()
        self.warsawMapQuery = overpass.MapQuery(52.0, 20.8, 52.4, 21.3)

    @staticmethod
    def addQuotesToJSONKeys(data: str) -> str:
        r = re.compile(r'(?P<separator>[{,])(?P<key>[a-zA-Z]+):')
        return r.sub(r'\g<separator>"\g<key>":', data)

    @staticmethod
    def downloadData(theme: str) -> str:
        return requests.post("https://mapa.um.warszawa.pl/mapviewer/foi", dict(
            request="getfoi",
            version="1.0",
            bbox="0:1787369:9500502:9791137",
            width=1,
            height=1,
            theme=theme,
            dstsrid=2178,
            cachefoi="yes",
            tid="2_7791522485845669270",
            aw="no",
        )).text

    def downloadDataWithCache(self, theme: str):
        rawDir = Path("raw")
        jsonDir = Path("json")
        rawDir.mkdir(exist_ok=True)
        jsonDir.mkdir(exist_ok=True)
        rawOutputPath = rawDir / (theme + ".raw")
        jsonOutputPath = jsonDir / (theme + ".json")
        if not rawOutputPath.exists() or not self.cacheEnabled:
            rawOutputPath.write_text(self.downloadData(theme))
        if not jsonOutputPath.exists() or not self.cacheEnabled:
            jsonOutputPath.write_text(self.addQuotesToJSONKeys(rawOutputPath.read_text()))
        umData = json.loads(jsonOutputPath.read_text())["foiarray"]
        return list(map(lambda p: dict(x=p["x"], y=p["y"]), umData))

    @staticmethod
    def elementQuery(overpassQuery: List[Tuple[str, str]]):
        return "".join([
            f'["{tag}"="{value}"]' for (tag, value) in overpassQuery
        ])

    def downloadOverpassData(self, overpassQuery: List[Tuple[str, str]]):
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
        overpassOutputPath = overpassDir / (queryHash + ".json")
        if not overpassOutputPath.exists() or not self.cacheEnabled:
            overpassResult = self.overpassApi.query(query)
            print(overpassResult)
            print(overpassResult.nodes)
            print(overpassResult.ways)
            result = []
            for node in overpassResult.nodes:
                result.append(dict(lat=float(node.lat), lon=float(node.lon)))
            for way in overpassResult.ways:
                result.append(dict(lat=float(way.center_lat), lon=float(way.center_lon.real)))
            json.dump(result, overpassOutputPath.open("w"))
        return json.load(overpassOutputPath.open("r"))

    @staticmethod
    def writeCSV(theme: str, outputTag: Tuple[str, str], data):
        csvDir = Path("output")
        csvDir.mkdir(exist_ok=True)
        csvOutputPath = csvDir / (theme + ".csv")
        csvWriter = csv.writer(csvOutputPath.open("w"), delimiter=";", quotechar='"')
        csvWriter.writerow(["latitude", "longitude", outputTag[0]])
        for (lat, lng) in data:
            csvWriter.writerow([lat, lng, outputTag[1]])

    def removeLikelyDuplicates(self, overpassData, umData):
        result = []
        for point in umData:
            lat, lng = self.transformer.transform(point["y"], point["x"])
            minDistance = DISTANCE_THRESHOLD + 1
            for osm in overpassData:
                minDistance = min(minDistance, self.wgs84Geod.inv(lng, lat, osm["lon"], osm["lat"])[2])
                if minDistance <= DISTANCE_THRESHOLD:
                    break
            if minDistance > DISTANCE_THRESHOLD:
                result.append((lat, lng))
        return result

    def process(self, theme: str, overpassQuery: List[Tuple[str, str]], outputTag: Tuple[str, str] = DEFAULT_TAG):
        umData = self.downloadDataWithCache(theme)
        overpassData = self.downloadOverpassData(overpassQuery=overpassQuery)
        deduplicatedData = self.removeLikelyDuplicates(overpassData=overpassData, umData=umData)
        self.writeCSV(theme=theme, data=deduplicatedData, outputTag=outputTag)


def main():
    dataSets = [
        ("dane_wawa.S_BIEZNIE", [("leisure", "track")]),
        ("dane_wawa.ROWERY_STOJAKI_ROWEROWE", [("amenity", "bicycle_parking")]),
    ]
    for (theme, overpassQuery) in tqdm(dataSets):
        UMWarszawaToCSV().process(theme=theme, overpassQuery=overpassQuery)


if __name__ == "__main__":
    main()
