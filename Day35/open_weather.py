from datetime import datetime
from typing import List
import requests


class OpenWeather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org"

    def get_weather_for_city(self, lat: float, lon: float) -> dict:
        params = dict(lat=lat, lon=lon, appid=self.api_key)
        url = f'{self.base_url}/data/2.5/weather'
        try:
            response = requests.get(url=url, params=params)
            return response.json()
        except Exception as e:
            print(e)
            return {}

    def get_hourly_forecast_data(self, lat: float, lon: float) -> dict:
        params = dict(lat=lat, lon=lon, appid=self.api_key)
        url = f'{self.base_url}/data/2.5/forecast'
        try:
            response = requests.get(url=url, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(e)
            return {}

    def parse_hour(self, item: dict) -> dict:
        ts = datetime.fromtimestamp(item["dt"]).isoformat()
        weather_id = item["weather"][0]["id"]
        weather = item["weather"][0]["main"]
        description = item["weather"][0]["description"]
        return dict(ts=ts, weather=weather, description=description, weather_id=weather_id)

    def parse_hourly_forecast_data(self, data: dict) -> List[dict]:
        return [self.parse_hour(item) for item in data["list"][:4]]
