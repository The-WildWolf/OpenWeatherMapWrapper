from openweathermapwrapper.weather import Weather

class ClothingSuggestions:
    """Provides clothing suggestions based on current weather data.

    This class takes a Weather instance, a city, and a country code as input,
    and provides clothing suggestions based on the current temperature and
    weather condition.

    Attributes:
        weather (Weather): An instance of the Weather class.
        city (str): The name of the city.
        country_code (str): The two-letter country code.
    """

    def __init__(self, weather: Weather, city: str, country_code: str):
        """Initialize the ClothingSuggestions with the provided Weather instance, city, and country code.

        Args:
            weather (Weather): An instance of the Weather class.
            city (str): The name of the city.
            country_code (str): The two-letter country code.
        """
        self.weather = weather
        self.city = city
        self.country_code = country_code

    def get_temperature_based_suggestions(self) -> str:
        """Provide clothing suggestions based on the current temperature.

        Returns:
            str: A string containing clothing suggestions based on the current temperature.
        """
        temp = self.weather.get_temperature(self.city, self.country_code)

        if temp <= 0:
            return "Wear a heavy coat, gloves, and a hat."
        elif 0 < temp <= 10:
            return "Wear a coat, a sweater, and a scarf."
        elif 10 < temp <= 20:
            return "Wear a light jacket or a sweater."
        else:
            return "Wear a t-shirt or a light blouse."

    def get_raw_temperature_based_suggestions(self) -> str:
        """Return a string representation of the temperature category.

        Returns:
            str: A string representing the temperature category, such as "temp_below_zero" or "temp_above_room_temperature".
        """
        temp = self.weather.get_temperature(self.city, self.country_code)

        if temp <= 0:
            return "temp_below_zero"
        elif 0 < temp <= 10:
            return "temp_below_10"
        elif 10 < temp <= 20:
            return "temp_below_20"
        else:
            return "temp_above_room_temperature"

    def get_condition_based_suggestions(self) -> str:
        """Provide clothing suggestions based on the current weather condition.

        Returns:
            str: A string containing clothing suggestions based on the current weather condition.
        """
        condition = self.weather.get_weather_condition(self.city, self.country_code)

        if "rain" in condition:
            return "Bring an umbrella and wear waterproof shoes."
        elif "snow" in condition:
            return "Wear warm and waterproof shoes, and consider bringing an umbrella."
        else:
            return "No special clothing required for current weather conditions."

    def get_raw_condition_based_suggestions(self) -> str:
        """Return a string representation of the weather condition category.

        Returns:
            str: A string representing the weather condition category, such as "rain", "snow", or "no_special".
        """
        condition = self.weather.get_weather_condition(self.city, self.country_code)

        if "rain" in condition:
            return "rain"
        elif "snow" in condition:
            return "snow"
        else:
            return "no_special"
