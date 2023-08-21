from typing import List
from open_weather import OpenWeather
from dotenv import load_dotenv
import os


def check_if_its_gonna_rain(hourly_data: List[dict]) -> bool:
    for three_hour in hourly_data:
        if three_hour["weather_id"] < 700:
            return True

    return False


def main():
    load_dotenv()
    api_key = os.getenv("OPEN_WEATHER_API_KEY")
    open_weather = OpenWeather(api_key)
    lat, lng = 61.924110, 25.748152
    hourly_data = open_weather.get_hourly_forecast_data(lat, lng)
    parsed = open_weather.parse_hourly_forecast_data(hourly_data)
    print(check_if_its_gonna_rain(parsed))


if __name__ == "__main__":
    main()
