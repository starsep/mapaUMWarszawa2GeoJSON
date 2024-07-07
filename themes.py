from models import ThemeCollection, Theme

themes = [
    ThemeCollection(
        name="Administracja",
        themes=[
            Theme(
                umKey="A_AMBASADY_N",
                name="Ambasady",
                iconUrl="https://mapa.um.warszawa.pl/mapaApp/Styles/Img/warstwy/1_administracja/49_ambasada.png",
            ),
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
                umKey="A_KONSULATY",
                name="Konsulaty",
                iconUrl="https://mapa.um.warszawa.pl/mapaApp/Styles/Img/warstwy/1_administracja/52_konsulat.png",
            ),
            Theme(
                umKey="A_PLACOWKI_POCZTOWE",
                name="Placówki pocztowe",
                iconUrl="https://mapa.um.warszawa.pl/mapaApp/Styles/Img/warstwy/1_administracja/59_poczta.png",
            ),
            Theme(
                umKey="A_PLACOWKI_ZUS",
                name="Placówki ZUS",
                iconUrl="https://mapa.um.warszawa.pl/mapaApp/Styles/Img/warstwy/1_administracja/zus.png",
            ),
            Theme(
                umKey="A_SADY",
                name="Sądy",
                iconUrl="https://mapa.um.warszawa.pl/mapaApp/Styles/Img/warstwy/1_administracja/55_sad.png",
            ),
            Theme(
                umKey="A_URZEDY_DZIELNIC_N",
                name="Urzędy Dzielnic",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.A_URZAD_DZIELNICY_N&w=100&h=90&ds=dane_wawa",
            ),
            Theme(
                umKey="A_URZEDY_SKARBOWE",
                name="Urzędy Skarbowe",
                iconUrl="https://mapa.um.warszawa.pl/mapaApp/Styles/Img/warstwy/1_administracja/urzad_skarbowy.png",
            ),
            Theme(
                umKey="A_USC_N",
                name="Urzędy Stanu Cywilnego",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.A_USC_N&w=100&h=90&ds=dane_wawa",
            ),
        ],
    ),
    ThemeCollection(
        name="Handel",
        themes=[
            Theme(
                umKey="HANDEL_STANOWISKA_POINT_N",
                name="Stanowiska handlowe",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.HANDEL_STANOWISKO_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="HANDEL_TARGOWISKA_JEDN_POINT_N",
                name="Targowiska jednodniowe",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.HANDEL_TARGOWISKO_JEDN_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="HANDEL_TARGOWISKA_N",
                name="Targowiska stałe",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.HANDEL_TARGOWISKO_N&w=100&h=100&ds=dane_wawa",
            ),
        ],
    ),
    ThemeCollection(
        name="Kultura",
        themes=[
            Theme(
                umKey="KU_BIBLIOTEKI_N",
                name="Biblioteki",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.KU_BIBLIOTEKI_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="KU_DOMY_KULTURY",
                name="Domy kultury",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.KU_DOMY_KULTURY_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="KU_KINA_N",
                name="Kina",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.KU_KINO_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="KU_MUZEA",
                name="Muzea",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.KU_MUZEUM_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="KU_POMNIKI_ZKP",
                name="Pomniki",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.POMNIKI&w=25&h=25&ds=dane_wawa",
            ),
            Theme(
                umKey="KU_SALE_KONCERTOWE",
                name="Sale koncertowe",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.KU_SALA_KONCERTOWA_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="KU_TABLICE_ZKP",
                name="Tablice",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.TABLICE&w=25&h=25&ds=dane_wawa",
            ),
            Theme(
                umKey="KU_TEATRY",
                name="Teatry",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.KU_TEATR_N&w=100&h=100&ds=dane_wawa",
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
                iconUrl="https://mapa.um.warszawa.pl/mapaApp/Styles/Img/warstwy/zezwolenia_alk/gastronomia.png",
            ),
            Theme(
                umKey="ZEZWOLENIA_ALKOHOLOWE_GASTRO_A",
                name="Zezwolenia alkoholowe gastronowia (piwo)",
                iconUrl="https://mapa.um.warszawa.pl/mapaApp/Styles/Img/warstwy/zezwolenia_alk/gastronomia.png",
            ),
            Theme(
                umKey="ZEZWOLENIA_ALKOHOLOWE_DETAL",
                name="Zezwolenia alkoholowe detal (inne)",
                iconUrl="https://mapa.um.warszawa.pl/mapaApp/Styles/Img/warstwy/zezwolenia_alk/detal.png",
            ),
            Theme(
                umKey="ZEZWOLENIA_ALKOHOLOWE_DETAL_A",
                name="Zezwolenia alkoholowe detal (piwo)",
                iconUrl="https://mapa.um.warszawa.pl/mapaApp/Styles/Img/warstwy/zezwolenia_alk/detal.png",
            ),
        ],
    ),
    ThemeCollection(
        name="Rowery",
        themes=[
            Theme(umKey="ROWERY_STOJAKI_ROWEROWE", name="Stojaki rowerowe"),
            Theme(
                umKey="ROWERY_STACJE_ROWEROWE",
                name="Stacje rowerów miejskich",
                iconUrl="https://testmapa.um.warszawa.pl/pliki/warstwy_grafika/rowery/rowery_stacje_rowerow.png",
            ),
            Theme(
                umKey="ROWERY_TOWAROWE_N",
                name="Wypożyczalnie rowerów towarowych",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.ROWER_TOWAROWY_N&w=100&h=100&ds=dane_wawa",
            ),
        ],
    ),
    ThemeCollection(
        name="Turystyka",
        themes=[
            Theme(
                umKey="T_AKADEMIKI",
                name="Akademiki",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.AKADEMIKI_25&w=100&h=100&ds=ZZP",
            ),
            Theme(
                umKey="T_APARTAMENTY",
                name="Apartamenty",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.APARTAMENTY_25&w=100&h=100&ds=ZZP",
            ),
            Theme(
                umKey="T_CAMPINGI",
                name="Kempingi",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.KEMPINGI_25&w=100&h=100&ds=ZZP",
            ),
            Theme(
                umKey="T_HOTELE",
                name="Hotele",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.HOTELE_25&w=100&h=100&ds=ZZP",
            ),
            Theme(
                umKey="T_SCHRONISKA",
                name="Schroniska i Hostele",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.SCHRONISKA_25&w=100&h=100&ds=ZZP",
            ),
        ],
    ),
    ThemeCollection(
        name="Transport publiczny",
        themes=[
            Theme(
                umKey="K_ZTM_BILETOMATY_KOLEJOWE_N",
                name="Biletomaty kolejowe WTP",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.K_PKP_BILETOMATY_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="K_ZTM_BILETOMATY_STACJONARNE_N",
                name="Biletomaty stacjonarne WTP",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.K_ZTM_BILETOMATY_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="K_DWORCE_KOLEJOWE_N",
                name="Dworce kolejowe",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.K_DWORZEC_KOLEJOWY_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="K_PROMY_N",
                name="Promy dla pieszych i rowerzystów",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.K_PROM_SYMBOL_N&w=100&h=100&ds=dane_wawa",
            ),
        ],
    ),
    ThemeCollection(
        name="Transport indywidualny",
        themes=[
            Theme(
                umKey="K_PARKOMATY_N",
                name="Parkomaty",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.K_PARKOMATY_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="K_PARKINGI_K_R_N",
                name="Strefy Kiss and Ride ",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.K_PARKING_K_R_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="K_PARKINGI_P_R_N",
                name="Parkingi Park and Ride",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.K_PARKING_P_R_N&w=100&h=100&ds=dane_wawa",
            ),
            Theme(
                umKey="K_PUNKTY_LADOWANIA_N",
                name="Punkty ładowania samochodów elektrycznych",
                iconUrl="https://testmapa.um.warszawa.pl/mapviewer/omserver?sty=M.K_PUNKT_LADOWANIA_N&w=100&h=100&ds=dane_wawa",
            ),
        ],
    ),
    ThemeCollection(
        name="Zieleń",
        themes=[
            Theme(
                umKey="BOS_ZIELEN_POMNIKI_NEW",
                name="Pomniki przyrody",
                iconUrl="https://testmapa.um.warszawa.pl/pliki/warstwy_grafika/bos_zielen/bos_zielen_pomnik.png",
            ),
        ],
    ),
    ThemeCollection(
        name="Inne",
        themes=[
            Theme(umKey="I_TOALETY", name="Toalety"),
            Theme(
                umKey="I_PLACE_ZABAW_POINT",
                name="Place zabaw",
                iconUrl="https://mapa.um.warszawa.pl/mapaApp/Styles/Img/warstwy/b_inne/M.PLACE_ZABAW.png",
            ),
        ],
    ),
]
