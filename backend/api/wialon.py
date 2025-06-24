from fastapi import APIRouter, Depends
from modules.auth import verify_token
from modules.wialon import get_wialon_data

router = APIRouter()

@router.get("/{vehicle_id}", dependencies=[Depends(verify_token)])
def wialon(vehicle_id: int):
    return get_wialon_data(vehicle_id)