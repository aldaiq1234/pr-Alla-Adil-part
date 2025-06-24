
import requests

def get_weather_data(city: str, api_key: str = "demo") -> dict:
    return {
        "city": city,
        "temperature": 23.5,
        "wind_speed": 4.2,
        "weather": "Clear"
    }
