from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Theme:
    umKey: str
    name: str
    iconUrl: str | None = None

    def defaultIconUrl(self):
        return f"https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.{self.umKey}&w=32&h=32&ds=dane_wawa"

    def downloadIconUrl(self):
        return self.iconUrl or self.defaultIconUrl()

    def outputFile(self, testMapDir: Path):
        return testMapDir / (self.umKey + ".geojson")

    def __str__(self):
        return super().__str__().replace(", iconUrl=None", "")


@dataclass(frozen=True)
class ThemeCollection:
    name: str
    themes: list[Theme]


@dataclass(frozen=True)
class ThemeResult:
    theme: Theme
    size: str
    themeCollectionName: str
    osmTags: list[list[str]]
    deduplicatedSize: str | None


@dataclass(frozen=True)
class ThemeCollectionResult:
    themeCollectionName: str
    themes: list[ThemeResult]

    @property
    def displayOsmTags(self):
        return any(len(theme.osmTags) > 0 for theme in self.themes)
