#!/usr/bin/env python3

from pathlib import Path
from pyproj import Transformer, CRS

import geojson

transformer = Transformer.from_crs(CRS("epsg:2178"), "wgs84")


def transformCoords(coords: list[float]) -> list[float]:
    result = []
    for i in range(0, len(coords), 2):
        lat, lng = transformer.transform(coords[i + 1], coords[i])
        result.append([lng, lat])
    return result


def convertGeojson(inputPath: Path, output: Path):
    with inputPath.open() as f:
        data = geojson.load(f)
    if "bbox" in data:
        data.bbox = transformCoords(data.bbox)
    for feature in data.features:
        if "label_box" in feature:
            feature.label_box = transformCoords(feature.label_box)
        match feature.geometry.type:
            case "Polygon":
                newGeometry = []
                for line in feature.geometry.coordinates:
                    newGeometry.append(transformCoords(line))
                feature.geometry.coordinates = newGeometry
                break
            case t:
                raise Exception(f"Unsupported type {t}")
    with output.open("w") as f:
        geojson.dump(data, f)


if __name__ == "__main__":
    convertGeojson(Path("example.geojson"), Path("output.geojson"))
