import requests
from open_weather import OpenWeather
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    open_weather = OpenWeather(api_key)
    resp = open_weather.get_weather_for_city(32.085300, 34.781769)
    print(resp)


if __name__ == "__main__":
    main()
