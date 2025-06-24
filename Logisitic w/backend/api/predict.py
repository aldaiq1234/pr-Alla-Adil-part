from fastapi import APIRouter, Depends
from schemas import PredictInput, PredictOutput
import joblib
from modules.auth import verify_token
from modules.fallback import fallback_predict

router = APIRouter()

@router.post("/", response_model=PredictOutput, dependencies=[Depends(verify_token)])
def predict(data: PredictInput):
    try:
        model = joblib.load("models/fuel_model_LinearRegression.pkl")
        X = [[data.distance_km, data.avg_speed, data.cargo_weight_tons, data.temperature]]
        pred = model.predict(X)[0]
    except:
        pred = fallback_predict(data.distance_km)
    return {"predicted_fuel": round(pred, 2)}