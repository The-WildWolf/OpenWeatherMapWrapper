import unittest
from unittest.mock import MagicMock

from openweathermapwrapper.clothing import ClothingSuggestions
from openweathermapwrapper.weather import Weather

class TestClothingSuggestions(unittest.TestCase):

    def setUp(self):
        self.weather_mock = MagicMock(spec=Weather)
        self.city = "London"
        self.country_code = "GB"
        self.suggestions = ClothingSuggestions(self.weather_mock, self.city, self.country_code)

    def test_get_temperature_based_suggestions(self):
        self.weather_mock.get_temperature.return_value = -5
        self.assertEqual(self.suggestions.get_temperature_based_suggestions(), "Wear a heavy coat, gloves, and a hat.")

        self.weather_mock.get_temperature.return_value = 5
        self.assertEqual(self.suggestions.get_temperature_based_suggestions(), "Wear a coat, a sweater, and a scarf.")

        self.weather_mock.get_temperature.return_value = 15
        self.assertEqual(self.suggestions.get_temperature_based_suggestions(), "Wear a light jacket or a sweater.")

        self.weather_mock.get_temperature.return_value = 25
        self.assertEqual(self.suggestions.get_temperature_based_suggestions(), "Wear a t-shirt or a light blouse.")

    def test_get_condition_based_suggestions(self):
        self.weather_mock.get_weather_condition.return_value = "light rain"
        self.assertEqual(self.suggestions.get_condition_based_suggestions(), "Bring an umbrella and wear waterproof shoes.")

        self.weather_mock.get_weather_condition.return_value = "heavy snow"
        self.assertEqual(self.suggestions.get_condition_based_suggestions(), "Wear warm and waterproof shoes, and consider bringing an umbrella.")

        self.weather_mock.get_weather_condition.return_value = "clear sky"
        self.assertEqual(self.suggestions.get_condition_based_suggestions(), "No special clothing required for current weather conditions.")

    def test_get_raw_temperature_based_suggestions(self):
        self.weather_mock.get_temperature.return_value = -5
        self.assertEqual(self.suggestions.get_raw_temperature_based_suggestions(), "temp_below_zero")

        self.weather_mock.get_temperature.return_value = 5
        self.assertEqual(self.suggestions.get_raw_temperature_based_suggestions(), "temp_below_10")

        self.weather_mock.get_temperature.return_value = 15
        self.assertEqual(self.suggestions.get_raw_temperature_based_suggestions(), "temp_below_20")

        self.weather_mock.get_temperature.return_value = 25
        self.assertEqual(self.suggestions.get_raw_temperature_based_suggestions(), "temp_above_room_temperature")

    def test_get_raw_condition_based_suggestions(self):
        self.weather_mock.get_weather_condition.return_value = "light rain"
        self.assertEqual(self.suggestions.get_raw_condition_based_suggestions(), "rain")

        self.weather_mock.get_weather_condition.return_value = "heavy snow"
        self.assertEqual(self.suggestions.get_raw_condition_based_suggestions(), "snow")

        self.weather_mock.get_weather_condition.return_value = "clear sky"
        self.assertEqual(self.suggestions.get_raw_condition_based_suggestions(), "no_special")

if __name__ == "__main__":
    unittest.main()
