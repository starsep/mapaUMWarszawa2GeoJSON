#!/usr/bin/env python3
from unittest import TestCase

from umWarszawa2GeoJSON import UMWarszawa2GeoJSON


class AddQuotesToJSONKeysTestCase(TestCase):
    def test_empty(self):
        self.assertEqual("", UMWarszawa2GeoJSON.addQuotesToJSONKeys(""))

    def test_example(self):
        self.assertEqual(
            '{"key":[{"id":"test","name":"name")',
            UMWarszawa2GeoJSON.addQuotesToJSONKeys('{"key":[{id:"test",name:"name")')
        )

    def test_separatorInValue(self):
        self.assertEqual(
            '{"key":"comma,test"',
            UMWarszawa2GeoJSON.addQuotesToJSONKeys('{key:"comma,test"')
        )


class TransformerTestCase(TestCase):
    def test_example(self):
        x, y = 5787262, 7498101
        lat, lng = UMWarszawa2GeoJSON().transformer.transform(x, y)
        self.assertAlmostEqual(lat, 52.218960, places=4)
        self.assertAlmostEqual(lng, 20.972205, places=4)
