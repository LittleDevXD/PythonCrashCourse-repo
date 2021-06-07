import unittest
from city_country import city_country

class CityCountryTest(unittest.TestCase):

    def test_city_country(self):
        formatted_value = city_country('new york', 'america')
        self.assertEqual(formatted_value, 'New York, America')
    
    def test_city_country_population(self):
        formatted_value = city_country('bago', 'myanmar', 1000_000)
        self.assertEqual(formatted_value, 'Bago, Myanmar - population 1000000')

if __name__ == '__main__':
    unittest.main()