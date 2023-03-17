import os
import requests

class OpenWeatherMapApiClient:
    """Client for interacting with the OpenWeatherMap API.

    This class provides methods for fetching the current weather and weather forecast
    for a specific city using the OpenWeatherMap API.

    Attributes:
        api_key (str): The API key to authenticate requests to the OpenWeatherMap API.
        current_weather_url (str): The base URL for the OpenWeatherMap current weather API endpoint.
        forecast_url (str): The base URL for the OpenWeatherMap forecast API endpoint.
    """

    def __init__(self, api_key: str = None):
        """Initialize the OpenWeatherMapApiClient with the provided API key or retrieve it from the environment variables.

        Args:
            api_key (str, optional): The API key for the OpenWeatherMap API. Defaults to None.

        Raises:
            ValueError: If the API key is not provided and not found in the environment variables.
        """
        if api_key is None:
            api_key = os.environ.get("OPENWEATHERMAP_API_KEY")

        if api_key is None:
            raise ValueError("API key not provided and not found in environment variables")

        self.api_key = api_key
        self.current_weather_url = "https://api.openweathermap.org/data/2.5/weather"
        self.forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

    def get_current_weather(self, city: str, country_code: str) -> dict:
        """Fetch the current weather for the specified city and country code.

        Args:
            city (str): The city name.
            country_code (str): The two-letter country code.

        Returns:
            dict: A dictionary containing the current weather data for the specified city and country code.

        Raises:
            requests.exceptions.HTTPError: If the API request results in an error.
        """
        params = {
            "q": f"{city},{country_code}",
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.current_weather_url, params=params)
        response.raise_for_status()

        return response.json()

    def get_forecast(self, city: str, country_code: str, date: str) -> dict:
        """Fetch the weather forecast for the specified city, country code, and date.

        Args:
            city (str): The city name.
            country_code (str): The two-letter country code.
            date (str): The date for which to fetch the forecast in the format "YYYY-MM-DD".

        Returns:
            dict: A dictionary containing the forecast data for the specified city, country code, and date.

        Raises:
            requests.exceptions.HTTPError: If the API request results in an error.
            ValueError: If no forecasts are found for the specified date.
        """
        params = {
            "q": f"{city},{country_code}",
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.forecast_url, params=params)
        response.raise_for_status()

        data = response.json()

        # Filter forecasts for the specified date
        forecasts = [forecast for forecast in data["list"] if forecast["dt_txt"].startswith(date)]

        if not forecasts:
            raise ValueError(f"No forecasts found for the date {date}")

        return forecasts[0]


