from pydantic import BaseModel

class PredictInput(BaseModel):
    distance_km: float
    avg_speed: float
    cargo_weight_tons: float
    temperature: float

class PredictOutput(BaseModel):
    predicted_fuel: float