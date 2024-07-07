from dataclasses import dataclass


@dataclass(frozen=True)
class Theme:
    umKey: str
    name: str
    iconUrl: str | None = None

    def defaultIconUrl(self):
        return f"https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.{self.umKey}&w=32&h=32&ds=dane_wawa"

    def downloadIconUrl(self):
        return self.iconUrl or self.defaultIconUrl()

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