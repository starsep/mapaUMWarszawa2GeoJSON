import asyncio
import dataclasses

import httpx

from models import Theme
from themes import themes

httpxClient = httpx.AsyncClient()


def _parseLayer(layer, testMapThemes: set[Theme]):
    if "szczegolyWarstwy" in layer:
        if "nazwaMVC" not in layer["szczegolyWarstwy"]:
            return
        iconUrl = None
        if "sciezkaDoPlikuSymbolu" in layer:
            iconUrl = layer["sciezkaDoPlikuSymbolu"]
            if "http" not in iconUrl:
                iconUrl = None
        theme = Theme(
            name=layer["nazwaOficjalna"]["pl"],
            umKey=layer["szczegolyWarstwy"]["nazwaMVC"],
            iconUrl=iconUrl,
        )
        if theme.iconUrl is not None and theme.iconUrl == theme.defaultIconUrl():
            theme = dataclasses.replace(theme, iconUrl=None)
        testMapThemes.add(theme)
    elif "warstwy" in layer:
        for subLayer in layer["warstwy"]:
            _parseLayer(subLayer, testMapThemes)


async def _getTestMapThemesForMap(mapId: str, testMapThemes: set[Theme]):
    response = await httpxClient.get(
        f"https://testmapa.um.warszawa.pl/api/modul-mapowy/open/mapy/{mapId}"
    )
    response.raise_for_status()
    layerCollections = response.json()["content"]["definicjaMapy"]["warstwy"]
    for layerCollection in layerCollections:
        if "Basic data" in layerCollection["nazwaOficjalna"]["en"]:
            continue
        for layer in layerCollection["warstwy"]:
            _parseLayer(layer, testMapThemes)


async def _getTestMapIds() -> list[str]:
    response = await httpxClient.get(
        "https://testmapa.um.warszawa.pl/api/modul-mapowy/open/kategorie-map/DESKTOPOWA"
    )
    response.raise_for_status()
    data = response.json()["content"]
    mapIds = set()
    for layerTypeName in data:
        layers = data[layerTypeName]
        if "grupyMap" in layers:
            for mapGroup in layers["grupyMap"]:
                mapIds.add(mapGroup["uuidMapy"])
        elif isinstance(layers, list):
            for i in range(len(layers)):
                for mapGroup in layers[i]["grupyMap"]:
                    mapIds.add(mapGroup["uuidMapy"])
    return sorted(list(mapIds))


async def getMissingTestMapThemes() -> list[Theme]:
    existingThemeKeys = {
        theme.umKey for collection in themes for theme in collection.themes
    }
    mapIds = await _getTestMapIds()
    testMapThemes: set[Theme] = set()
    for mapId in mapIds:
        try:
            await _getTestMapThemesForMap(mapId, testMapThemes)
        except Exception as e:
            print(f"Failed to get layers for {mapId}: {e}")
    return sorted(
        [theme for theme in testMapThemes if theme.umKey not in existingThemeKeys],
        key=lambda theme: theme.umKey,
    )


async def main():
    missingThemes = await getMissingTestMapThemes()
    for theme in missingThemes:
        print(f"{theme},")


if __name__ == "__main__":
    asyncio.run(main())
