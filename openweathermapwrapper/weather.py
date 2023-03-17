from openweathermapwrapper.api_client import OpenWeatherMapApiClient


class Weather:
    """Provides weather data using the OpenWeatherMapApiClient.

    This class retrieves weather data, including temperature and weather conditions,
    for a given city and country code using the OpenWeatherMapApiClient.

    Attributes:
        client (OpenWeatherMapApiClient): An instance of the OpenWeatherMapApiClient.
    """
    def __init__(self):
        """Initialize the Weather class with an instance of OpenWeatherMapApiClient."""
        self.client = OpenWeatherMapApiClient()

    def get_temperature(self, city: str, country_code: str) -> float:
        """Retrieve the current temperature for the specified city and country code.

        Args:
            city (str): The name of the city.
            country_code (str): The two-letter country code.

        Returns:
            float: The current temperature in the specified city and country code.
        """
        current_weather = self.client.get_current_weather(city, country_code)
        return current_weather["main"]["temp"]

    def get_weather_condition(self, city: str, country_code: str) -> str:
        """Retrieve the current weather condition for the specified city and country code.

        Args:
            city (str): The name of the city.
            country_code (str): The two-letter country code.

        Returns:
            str: The current weather condition in the specified city and country code.
        """
        current_weather = self.client.get_current_weather(city, country_code)
        return current_weather["weather"][0]["description"]