import os
import unittest
from unittest.mock import patch, Mock

from openweathermapwrapper.api_client import OpenWeatherMapApiClient


class TestOpenWeatherMapApiClient(unittest.TestCase):
    def setUp(self):
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
        self.city = "London"
        self.country_code = "GB"
        self.date = "2023-03-20"

    def test_get_current_weather_success(self):
        mock_json = {
            "coord": {"lon": -0.1257, "lat": 51.5085},
            "weather": [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04n"}],
            "base": "stations",
            "main": {"temp": 7.52, "feels_like": 6.03, "temp_min": 7, "temp_max": 8.24, "pressure": 1019, "humidity": 96},
            "visibility": 10000,
            "wind": {"speed": 1.54, "deg": 60},
            "clouds": {"all": 90},
            "dt": 1679587657,
            "sys": {"type": 2, "id": 2019646, "country": "GB", "sunrise": 1679533203, "sunset": 1679570623},
            "timezone": 3600,
            "id": 2643743,
            "name": "London",
            "cod": 200
        }

        with patch("requests.get") as mock_get:
            mock_get.return_value = Mock(status_code=200, json=lambda: mock_json)

            owm_client = OpenWeatherMapApiClient(api_key=self.api_key)
            result = owm_client.get_current_weather(self.city, self.country_code)
            self.assertEqual(result, mock_json)

    def test_get_forecast_success(self):
        mock_json = {
            "list": [
                {
                    "dt": 1679602800,
                    "main": {"temp": 7.6, "feels_like": 6.09, "pressure": 1019, "humidity": 97},
                    "weather": [{"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04n"}],
                    "clouds": {"all": 91},
                    "wind": {"speed": 1.54, "deg": 60},
                    "visibility": 10000,
                    "pop": 0.04,
                    "sys": {"pod": "n"},
                    "dt_txt": "2023-03-20 00:00:00"
                }
            ]
        }

        with patch("requests.get") as mock_get:
            mock_get.return_value = Mock(status_code=200, json=lambda: mock_json)

            owm_client = OpenWeatherMapApiClient(api_key=self.api_key)
            result = owm_client.get_forecast(self.city, self.country_code, self.date)
            self.assertEqual(result, mock_json["list"][0])

    def test_get_forecast_no_forecast_found(self):
        mock_json = {"list": []}

        with patch("requests.get") as mock_get:
            mock_get.return_value = Mock(status_code=200, json=lambda: mock_json)

            owm_client = OpenWeatherMapApiClient(api_key=self.api_key)

            with self.assertRaises(ValueError):
                owm_client.get_forecast(self.city, self.country_code, self.date)

if __name__ == '__main__':
    unittest.main()
