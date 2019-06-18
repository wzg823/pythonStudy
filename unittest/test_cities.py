import unittest
from city_function import city_country_name

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_name = city_country_name('beijing','china')
        self.assertEqual(formatted_name,'Beijing China')
    def test_city_country_population(self):
        formatted_name = city_country_name('beijing','china',50000000)
        self.assertEqual(formatted_name,'Beijing China -Population 50000000')

unittest.main()