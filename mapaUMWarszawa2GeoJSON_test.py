from mapaUMWarszawa2GeoJSON import MapaUMWarszawa2GeoJSON
import pytest


def testAddQuotesToJSONKeys_empty():
    assert MapaUMWarszawa2GeoJSON.addQuotesToJSONKeys("") == ""


def testAddQuotesToJSONKeys_example():
    assert (
        MapaUMWarszawa2GeoJSON.addQuotesToJSONKeys('{"key":[{id:"test",name:"name")')
        == '{"key":[{"id":"test","name":"name")'
    )


def testAddQuotesToJSONKeysTestCase_separatorInValue():
    assert (
        MapaUMWarszawa2GeoJSON.addQuotesToJSONKeys('{key:"comma,test"')
        == '{"key":"comma,test"'
    )


def testTransformer_example():
    x, y = 5787262, 7498101
    lat, lng = MapaUMWarszawa2GeoJSON().transformer.transform(x, y)
    assert lat == pytest.approx(52.218960, abs=1e-4)
    assert lng == pytest.approx(20.972205, abs=1e-4)


def testParseName_simple():
    name = """Godziny otwarcia: całodobowo
Dostępność dla niepełnosprawnych: nie
Płatna: nie
Przewijak: nie"""
    expected = {
        "Godziny otwarcia": "całodobowo",
        "Dostępność dla niepełnosprawnych": "nie",
        "Płatna": "nie",
        "Przewijak": "nie",
    }
    assert MapaUMWarszawa2GeoJSON().parseTagsFromName(name) == expected


def testParseName_multiline():
    name = """Foo: bar
Lokalizacja: Ochota
Przykładowa ulica, nr
Dodatkowe informacje
Tag: wartość"""
    expected = {
        "Foo": "bar",
        "Lokalizacja": """Ochota
Przykładowa ulica, nr
Dodatkowe informacje""",
        "Tag": "wartość",
    }
    assert MapaUMWarszawa2GeoJSON().parseTagsFromName(name) == expected
