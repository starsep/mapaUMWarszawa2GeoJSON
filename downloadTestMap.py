#!/usr/bin/env python3
import asyncio
import logging
from pathlib import Path

import geojson
import httpx
from tqdm.asyncio import tqdm

httpxClient = httpx.AsyncClient()


async def downloadDataTestMapa(theme: str):
    result = await httpxClient.post(
        "https://testmapa.um.warszawa.pl/mapviewer/dataserver/DANE_WAWA",
        headers={
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        },
        params=dict(
            t=theme,
            include_label_box="false",
            to_srid="4326",
            bbox_srid="4326",
        ),
    )
    result.raise_for_status()
    data = result.json()
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


async def main():
    SPORT_ATHLETICS = ("sport", "athletics")
    SPORT_UNKNOWN = ("sport", "fake")
    FITNESS_CENTRE = ("leisure", "fitness_centre")
    dataSets: list[tuple[str, str]] = [
        ("I_TOALETY", [("amenity", "toilets")]),
        ("BOS_ZIELEN_POMNIKI_SM_NEW", [("denotation", "natural_monument")]),
        ("BOS_ZIELEN_POMNIKI_NEW", [("denotation", "natural_monument")]),
        ("ZEZWOLENIA_ALKOHOLOWE_GASTRO", []),
        ("ZEZWOLENIA_ALKOHOLOWE_GASTRO_A", []),
        ("ZEZWOLENIA_ALKOHOLOWE_DETAL", []),
        ("ZEZWOLENIA_ALKOHOLOWE_DETAL_A", []),
        ("KU_POMNIKI", []),
        ("KU_TABLICE", []),
        (
            "K_ZTM_BILETOMATY_STACJONARNE",
            [("vending", "public_transport_tickets")],
        ),
        ("ROWERY_STOJAKI_ROWEROWE", [("amenity", "bicycle_parking")]),
        ("I_PLACE_ZABAW_POINT", [("leisure", "playground")]),
        ("S_BIEZNIE", [("leisure", "track")]),
        ("S_FITNESS", [FITNESS_CENTRE]),
        ("S_HALE_SPORTOWE", [("leisure", "sports_hall")]),
        ("S_INNE", [SPORT_UNKNOWN]),
        ("S_KORTY_TENISOWE", [("sport", "tennis")]),
        (
            "S_KOSZYKOWKA",
            [("leisure", "pitch")],
        ),
        ("S_KREGIELNIE", [("sport", "9pin")]),
        ("S_LODOWISKA", [("sport", "ice_skating")]),
        ("S_PCHNIECIE_KULA", [SPORT_UNKNOWN]),
        ("S_PILKA_NOZNA", [("sport", "soccer")]),
        ("S_PILKA_RECZNA", [("sport", "handball")]),
        ("S_PLYWALNIE_KRYTE", [("leisure", "swimming_pool")]),
        ("S_PLYWALNIE_ODKRYTE", [("leisure", "swimming_pool")]),
        ("S_SALE_GIMNASTYCZNE", [("sport", "gymnastics")]),
        ("S_SALE_I_PAWILONY", [SPORT_UNKNOWN]),
        ("S_SCIANKI_WSPINACZKOWE", [("sport", "climbing")]),
        ("S_SIATKOWKA", [("sport", "basketball")]),
        ("S_SILOWNIE", [FITNESS_CENTRE]),
        ("S_SILOWNIE_PLENEROWE", [FITNESS_CENTRE]),
        ("S_SKATEPARKI", [("sport", "skateboard")]),
        ("S_SKOKI_W_DAL", [SPORT_ATHLETICS]),
        ("S_SKOKI_WZWYZ", [SPORT_ATHLETICS]),
        ("S_SPORTY_LODZIOWE", [("sport", "sailing")]),
        ("S_SQUASH", [("sport", "squash")]),
        ("S_STADIONY_LA", [SPORT_ATHLETICS]),
        ("S_STRZELNICE", [("sport", "shooting")]),
        ("S_TORY", [SPORT_UNKNOWN]),
    ]

    async def processTheme(theme: str):
        try:
            testMapGeojsonDir = Path("testMapGeojson")
            testMapGeojsonDir.mkdir(exist_ok=True)
            data = await downloadDataTestMapa(theme)
            with (testMapGeojsonDir / (theme + ".geojson")).open("w") as f:
                geojson.dump(data, f)
        except Exception as e:
            logging.error(f"Failed to download {theme}: {e}")
    await tqdm.gather(*[processTheme(theme) for theme, _ in dataSets])


if __name__ == "__main__":
    asyncio.run(main())
