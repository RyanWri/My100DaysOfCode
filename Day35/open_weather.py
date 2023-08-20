import requests


class OpenWeather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/"

    def get_weather_for_city(self, lat: float, lon: float) -> dict:
        params = dict(lat=lat, lon=lon, appid=self.api_key)
        url = f'{self.base_url}/weather'
        try:
            response = requests.get(url=url, params=params)
            return response.json()
        except Exception as e:
            print(e)
            return {}
