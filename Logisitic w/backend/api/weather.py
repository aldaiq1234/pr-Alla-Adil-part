from fastapi import APIRouter, Depends
from modules.auth import verify_token
from modules.weather import get_weather_data

router = APIRouter()

@router.get("/{city}", dependencies=[Depends(verify_token)])
def weather(city: str):
    return get_weather_data(city)