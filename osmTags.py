SPORT_ATHLETICS = ["sport=athletics"]
FITNESS_CENTRE = ["leisure=fitness_centre"]
ALCOHOL_GASTRONOMY = [
    ['amenity~"(restaurant|bar|fast_food|cafe|pub|biergarten|nightclub)"'],
    ['shop~"(alcohol|wine|beverages|deli)"'],
    ["tourism=hotel"],
]
ALCOHOL_SHOPS = [
    ['amenity~"(bar|restaurant|cafe)"'],
    [
        'shop~"(alcohol|wine|beverages|deli|supermarket|convenience|tobacco|confectionery|houseware)"'
    ],
]
SWIMMING = [
    ['leisure~"(swimming_pool|water_park)"'],
    ["sport=swimming"],
]
BASKETBALL = [['sport~"(basketball|multi)"']]


def _generateOsmTags() -> dict[str, list[list[str]]]:
    result: dict[str, list[list[str]]] = {
        "A_AMBASADY_N": [["diplomatic=embassy"]],
        "A_BIURA_URZEDU_N": [["office=government"]],
        "A_JEDNOSTKI_ORG_URZEDU_N": [["office=government"]],
        "A_KONSULATY": [["diplomatic=consulate"]],
        "A_PLACOWKI_POCZTOWE": [["amenity=post_office"]],
        "A_PLACOWKI_ZUS": [["government=social_security"]],
        "A_SADY": [
            ["amenity=courthouse"],
            ["government=judicial"],
        ],
        "A_URZEDY_DZIELNIC_N": [["office=government"]],
        "A_URZEDY_SKARBOWE": [['government~"(customs|tax)"']],
        "A_USC_N": [["office=government"]],
        "BEZP_KAMERY_N": [["man_made=surveillance"]],
        "BEZP_POLICJA_N": [["amenity=police"]],
        "BEZP_PSP_N": [
            ["building=fire_station"],
            ["amenity=fire_station"],
        ],
        "BEZP_STRAZ_MIEJSKA_N": [["amenity=police"]],
        "BOS_ZIELEN_POMNIKI_NEW": [["denotation=natural_monument"]],
        "BOS_ZIELEN_POMNIKI_SM_NEW": [["denotation=natural_monument"]],
        "HANDEL_STANOWISKA_POINT_N": [["amenity=marketplace"]],
        "HANDEL_TARGOWISKA_JEDN_POINT_N": [["amenity=marketplace"]],
        "HANDEL_TARGOWISKA_N": [["amenity=marketplace"]],
        "I_PLACE_ZABAW_POINT": [["leisure=playground"]],
        "I_TOALETY": [["amenity=toilets"]],
        "K_ZTM_BILETOMATY_STACJONARNE": [["vending=public_transport_tickets"]],
        "K_ZTM_BILETOMATY_KOLEJOWE_N": [["vending=public_transport_tickets"]],
        "K_DWORCE_KOLEJOWE_N": [
            ['railway~"(station|halt)"'],
            ["building=train_station"],
        ],
        "K_PROMY_N": [["amenity=ferry_terminal"]],
        "K_PARKOMATY_N": [["vending=parking_tickets"]],
        "K_PARKINGI_K_R_N": [["amenity=parking"]],
        "K_PARKINGI_P_R_N": [["park_ride=yes"]],
        "K_PUNKTY_LADOWANIA_N": [["amenity=charging_station"]],
        "KU_BIBLIOTEKI_N": [["amenity=library"]],
        "KU_DOMY_KULTURY": [['amenity~"(arts_centre|community_centre)"']],
        "KU_KINA_N": [["amenity=cinema"]],
        "KU_MUZEA": [['tourism~"(museum|gallery)"']],
        "KU_POMNIKI_ZKP": [["historic=memorial"]],
        "KU_SALE_KONCERTOWE": [["amenity=theatre"]],
        "KU_TABLICE_ZKP": [["historic=memorial"]],
        "KU_TEATRY": [["amenity=theatre"]],
        "ROWERY_STOJAKI_ROWEROWE": [["amenity=bicycle_parking"]],
        "ROWERY_STACJE_ROWEROWE": [["amenity=bicycle_rental"]],
        "ROWERY_SERWISY_ROWEROWE_N": [['"service:bicycle:repair"=yes']],
        "ROWERY_STACJE_NAPRAW_N": [["amenity=bicycle_repair_station"]],
        "S_BIEZNIE_OKOLNE_BU_N": [["leisure=track"]],
        "S_BIEZNIE_PROSTE_BU_N": [["leisure=track"]],
        "S_BULODROM_N": [["sport=boules"]],
        "S_FITNESS": [FITNESS_CENTRE],
        "S_HALA_SPORTOWA_N": [["leisure=sports_hall"]],
        "S_HALE_SPORTOWE": [["leisure=sports_hall"]],
        "S_HOKEJ_TRAWA_BU_N": [["sport=field_hockey"]],
        "S_KORTY_TENISOWE_BU_N": [["sport=tennis"]],
        "S_KORTY_TENISOWE": [["sport=tennis"]],
        "S_KOSZYKOWKA_BU_N": BASKETBALL,
        "S_KOSZYKOWKA": BASKETBALL,
        "S_KREGIELNIE": [
            ["leisure=bowling_alley"],
            ['sport~"(8|9|10)pin"'],
        ],
        "S_LODOWISKA_N": [["sport=ice_skating"]],
        "S_LUCZNICTWO_N": [["sport=archery"]],
        "S_MINIGOLF_N": [["leisure=miniature_golf"]],
        "S_PCHNIECIE_KULA_N": [SPORT_ATHLETICS],
        "S_PILKA_NOZNA_BU_N": [["sport=soccer"]],
        "S_PILKA_NOZNA": [["sport=soccer"]],
        "S_PILKA_NOZNA_STADION_N": [["sport=soccer"]],
        "S_PILKA_RECZNA_BU_N": [["sport=handball"]],
        "S_PILKA_RECZNA_PLAZOWA_N": [["sport=handball"]],
        "S_PLYWALNIE_KRYTE": SWIMMING,
        "S_PLYWALNIE_ODKRYTE": SWIMMING,
        "S_PUMPTRUCK_N": [["cycling=pump_track"]],
        "S_RZUT_DYSKIEM_N": [SPORT_ATHLETICS],
        "S_SALE_GIMNASTYCZNE_N": [["sport=gymnastics"]],
        "S_SALE_GIMNASTYCZNE": [["sport=gymnastics"]],
        "S_SALE_POMOCNICZE_N": [FITNESS_CENTRE],
        "S_SAUNA_N": [
            ["leisure=sauna"],
            ["sauna", "sauna!=no"],
        ],
        "S_SCIANKA_TENIS_N": [["sport=tennis"]],
        "S_SCIANKI_WSPINACZKOWE": [["sport=climbing"]],
        "S_SIATKOWKA_BU_N": [["sport=volleyball"]],
        "S_SIATKOWKA_PLAZOWA_N": [["sport=volleyball"]],
        "S_SIATKOWKA": [["sport=volleyball"]],
        "S_SILOWNIE": [FITNESS_CENTRE],
        "S_SILOWNIE_PLENEROWE": [
            ["leisure=fitness_station"],
            ["sport=fitness"],
        ],
        "S_SKATEPARKI": [["sport=skateboard"]],
        "S_SKOKI_W_DAL": [SPORT_ATHLETICS],
        "S_SKOKI_WZWYZ": [SPORT_ATHLETICS],
        "S_SKOK_W_DAL_N": [SPORT_ATHLETICS],
        "S_SKOK_WZWYZ_N": [SPORT_ATHLETICS],
        "S_SPORTY_LODZIOWE": [["sport=sailing"]],
        "S_SQUASH": [["sport=squash"]],
        "S_STADIONY_LA": [SPORT_ATHLETICS],
        "S_STADIONY_LEKKOATLETYCZNE_N": [SPORT_ATHLETICS],
        "S_STREETWORKOUT_N": [["leisure=fitness_station"]],
        "S_STRZELNICE": [["sport=shooting"]],
        "S_TENIS_STOLOWY_N": [["sport=table_tennis"]],
        "S_TOR_LYZWIARSKI_N": [["sport=ice_skating"]],
        "S_TRASA_NARCIARSKA_N": [["sport=skiing"]],
        "S_TRASA_NARTOROLKOWA_N": [["sport=roller_skating"]],
        "T_AKADEMIKI": [["building=dormitory"]],
        "T_APARTAMENTY": [["tourism=apartment"]],
        "T_CAMPINGI": [["tourism=camp_site"]],
        "T_HOTELE": [["tourism=hotel"]],
        "T_SCHRONISKA": [["tourism=hostel"]],
        "ZEZWOLENIA_ALKOHOLOWE_DETAL": ALCOHOL_SHOPS,
        "ZEZWOLENIA_ALKOHOLOWE_DETAL_A": ALCOHOL_SHOPS,
        "ZEZWOLENIA_ALKOHOLOWE_GASTRO": ALCOHOL_GASTRONOMY,
        "ZEZWOLENIA_ALKOHOLOWE_GASTRO_A": ALCOHOL_GASTRONOMY,
    }
    for tag in list(result.keys()):
        if not tag.endswith("_N"):
            result[tag + "_N"] = result[tag]
    return result


osmTagsForTheme = _generateOsmTags()
