from models import ThemeCollection, Theme

themes = [
    ThemeCollection(
        name="Administracja",
        themes=[
            Theme(umKey="A_AMBASADY_N", name="Ambasady"),
            Theme(
                umKey="A_BIURA_URZEDU_N",
                name="Biura Urzędu",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.A_BIURA_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="A_JEDNOSTKI_ORG_URZEDU_N",
                name="Jednostki organizacyjne Urzędu",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.A_JEDNOSTKI_ORG_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="A_URZEDY_DZIELNIC_N",
                name="Urzędy Dzielnic",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.A_URZAD_DZIELNICY_N&w=100&h=90&ds=dane_wawa",
            ),
            Theme(
                umKey="A_USC_N",
                name="Urzędy Stanu Cywilnego",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.A_USC_N&w=100&h=90&ds=dane_wawa",
            ),
        ],
    ),
    ThemeCollection(
        name="Sport",
        themes=[
            Theme(
                umKey="S_BIEZNIE_OKOLNE_BU_N",
                name="Bieżnie okólne",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_BIEZNIA_N&w=32&h=32&ds=dane_wawa",
            ),
            Theme(
                umKey="S_BIEZNIE_PROSTE_BU_N",
                name="Bieżnie proste",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_BIEZNIA_N&w=32&h=32&ds=dane_wawa",
            ),
            Theme(umKey="S_BULODROM_N", name="Bulodromy"),
            Theme(umKey="S_HALA_SPORTOWA_N", name="Hale sportowe"),
            Theme(
                umKey="S_HOKEJ_TRAWA_BU_N",
                name="Boiska do hokeja na trawie",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_HOKEJ_TRAWA_N&w=32&h=32&ds=dane_wawa",
            ),
            Theme(
                umKey="S_KORTY_TENISOWE_BU_N",
                name="Korty tenisowe",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_KORTY_TENISOWE_N&w=32&h=32&ds=dane_wawa",
            ),
            Theme(
                umKey="S_KOSZYKOWKA_BU_N",
                name="Boiska do koszykówki",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_KOSZYKOWKA_N&w=32&h=32&ds=dane_wawa",
            ),
            Theme(umKey="S_KREGIELNIE_N", name="Kręgielnie"),
            Theme(umKey="S_LODOWISKA_N", name="Lodowiska"),
            Theme(umKey="S_LUCZNICTWO_N", name="Tory łucznicze"),
            Theme(umKey="S_MINIGOLF_N", name="Pola do minigolfa"),
            Theme(umKey="S_PCHNIECIE_KULA_N", name="Rzutnie do pchnięcia kulą"),
            Theme(
                umKey="S_PILKA_NOZNA_BU_N",
                name="Boiska piłkarskie",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_PILKA_NOZNA_N&w=32&h=32&ds=dane_wawa",
            ),
            Theme(umKey="S_PILKA_NOZNA_STADION_N", name="Stadiony piłkarskie"),
            Theme(
                umKey="S_PILKA_RECZNA_BU_N",
                name="Boiska do piłki ręcznej",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_PILKA_RECZNA_N&w=32&h=32&ds=dane_wawa",
            ),
            Theme(
                umKey="S_PILKA_RECZNA_PLAZOWA_N",
                name="Boiska do piłki ręcznej plażowej",
            ),
            Theme(umKey="S_PLYWALNIE_KRYTE_N", name="Pływalnie kryte"),
            Theme(
                umKey="S_PLYWALNIE_ODKRYTE_N",
                name="Pływalnie letnie",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_PLYWANIE_ODKRYTE_N&w=32&h=32&ds=dane_wawa",
            ),
            Theme(umKey="S_PUMPTRUCK_N", name="Pumptracki"),
            Theme(umKey="S_RICOCHET_N", name="Korty do ricocheta"),
            Theme(
                umKey="S_RZUT_DYSKIEM_N",
                name="Rzutnie do rzutu dyskiem",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_PCHNIECIE_KULA_N&w=32&h=32&ds=dane_wawa",
            ),
            Theme(umKey="S_SALE_GIMNASTYCZNE_N", name="Sale gimnastyczne"),
            Theme(
                umKey="S_SALE_POMOCNICZE_N",
                name="Sale fitness",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_SALE_FITNESS_N&w=32&h=32&ds=dane_wawa",
            ),
            Theme(umKey="S_SAUNA_N", name="Sauny"),
            Theme(umKey="S_SCIANKA_TENIS_N", name="Ścianki do tenisa"),
            Theme(umKey="S_SCIANKI_WSPINACZKOWE_N", name="Ścianki wspinaczkowe"),
            Theme(
                umKey="S_SIATKOWKA_BU_N",
                name="Boiska do piłki siatkowej",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_SIATKOWKA_N&w=32&h=32&ds=dane_wawa",
            ),
            Theme(
                umKey="S_SIATKOWKA_PLAZOWA_N", name="Boiska do piłki siatkowej plażowej"
            ),
            Theme(umKey="S_SILOWNIE_N", name="Siłownie"),
            Theme(umKey="S_SILOWNIE_PLENEROWE_N", name="Siłownie zewnętrzne"),
            Theme(umKey="S_SKATEPARKI_N", name="Skateparki"),
            Theme(umKey="S_SKOK_WZWYZ_N", name="Skocznie do skoku wzwyż"),
            Theme(umKey="S_SKOK_W_DAL_N", name="Skocznie do skoku w dal i trójskoku"),
            Theme(umKey="S_SQUASH_N", name="Korty do squasha"),
            Theme(
                umKey="S_STADIONY_LEKKOATLETYCZNE_N", name="Stadiony lekkoatletyczne"
            ),
            Theme(umKey="S_STREETWORKOUT_N", name="Street workout"),
            Theme(umKey="S_STRZELNICE_N", name="Strzelnice"),
            Theme(
                umKey="S_TENIS_STOLOWY_N", name="Stoły do tenisa stołowego zewnętrzne"
            ),
            Theme(umKey="S_TOR_LYZWIARSKI_N", name="Tory łyżwiarskie"),
            Theme(umKey="S_TOR_SANECZKOWY_N", name="Tory saneczkowe"),
            Theme(umKey="S_TRASA_NARCIARSKA_N", name="Narciarskie trasy zjazdowe"),
            Theme(
                umKey="S_TRASA_NARTOROLKOWA_N",
                name="Trasy nartorolkowe",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.S_TRASA_NARCIARSKA_N&w=32&h=32&ds=dane_wawa",
            ),
        ],
    ),
    ThemeCollection(
        name="Zezwolenia alkoholowe",
        themes=[
            Theme(
                umKey="ZEZWOLENIA_ALKOHOLOWE_GASTRO",
                name="Zezwolenia alkoholowe gastronowia (inne)",
            ),
            Theme(
                umKey="ZEZWOLENIA_ALKOHOLOWE_GASTRO_A",
                name="Zezwolenia alkoholowe gastronowia (piwo)",
            ),
            Theme(
                umKey="ZEZWOLENIA_ALKOHOLOWE_DETAL",
                name="Zezwolenia alkoholowe detal (inne)",
            ),
            Theme(
                umKey="ZEZWOLENIA_ALKOHOLOWE_DETAL_A",
                name="Zezwolenia alkoholowe detal (piwo)",
            ),
        ],
    ),
    ThemeCollection(
        name="Rowery",
        themes=[
            Theme(umKey="ROWERY_STOJAKI_ROWEROWE", name="Stojaki rowerowe"),
        ],
    ),
    ThemeCollection(
        name="Transport publiczny",
        themes=[
            Theme(
                umKey="K_ZTM_BILETOMATY_STACJONARNE", name="Biletomaty stacjonarne ZTM"
            ),
        ],
    ),
    ThemeCollection(
        name="Inne",
        themes=[
            Theme(umKey="I_TOALETY", name="Toalety"),
            Theme(
                umKey="BOS_ZIELEN_POMNIKI_SM_NEW",
                name="Pomniki przyrody, głazy narzutowe, inne",
            ),
            Theme(umKey="BOS_ZIELEN_POMNIKI_NEW", name="Pomniki przyrody"),
            Theme(umKey="KU_POMNIKI", name="Pomniki"),
            Theme(umKey="KU_TABLICE", name="Tablice"),
            Theme(umKey="I_PLACE_ZABAW_POINT", name="Place zabaw"),
        ],
    ),
]
