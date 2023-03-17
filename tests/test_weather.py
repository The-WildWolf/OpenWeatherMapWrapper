import unittest
from unittest.mock import MagicMock

from openweathermapwrapper.api_client import OpenWeatherMapApiClient
from openweathermapwrapper.weather import Weather


class TestWeather(unittest.TestCase):

    def setUp(self):
        self.api_client_mock = MagicMock(spec=OpenWeatherMapApiClient)
        self.weather = Weather()
        self.weather.client = self.api_client_mock

    def test_get_temperature(self):
        self.api_client_mock.get_current_weather.return_value = {
            "main": {"temp": 20.0},
            "weather": [{"description": "clear sky"}]
        }

        city = "London"
        country_code = "GB"
        temperature = self.weather.get_temperature(city, country_code)
        self.assertEqual(temperature, 20.0)

    def test_get_weather_condition(self):
        self.api_client_mock.get_current_weather.return_value = {
            "main": {"temp": 20.0},
            "weather": [{"description": "clear sky"}]
        }

        city = "London"
        country_code = "GB"
        condition = self.weather.get_weather_condition(city, country_code)
        self.assertEqual(condition, "clear sky")

if __name__ == "__main__":
    unittest.main()
