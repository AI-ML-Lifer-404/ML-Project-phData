from fastapi import APIRouter
from pydantic import BaseModel
import pickle
import pandas as pd
import csv


router = APIRouter()


class RealEstatePricePredictorRequest(BaseModel):
    bedrooms: int
    bathrooms: float
    sqft_living: int
    sqft_lot: int
    floors: float
    waterfront: int
    view: int
    grade: int
    sqft_above: int
    sqft_basement: int
    yr_built: int
    yr_renovated: int
    zipcode: int
    lat: float
    long: float
    sqft_living15: int
    sqft_lot15: int

    model_config = {
        "json_schema_extra": {
            "example": {
                "bedrooms": 4,
                "bathrooms": 1.00,
                "sqft_living": 2000,
                "sqft_lot": 6000,
                "floors": 2.4,
                "waterfront": 1,
                "view": 1,
                "grade": 7,
                "sqft_above": 2500,
                "sqft_basement": 300,
                "yr_built": 1985,
                "yr_renovated": 0,
                "zipcode": 98144,
                "lat": 47.2110,
                "long": -122.100,
                "sqft_living15": 2100,
                "sqft_lot15": 3000


            }
        }
    }


with open("/model/model.pkl", "rb") as f:
    model = pickle.load(f)


@router.post("/predict")
async def predict(features: RealEstatePricePredictorRequest):

    df = pd.DataFrame([features.model_dump().values()])

    pred = model.predict(df)
    return {"pred": int(pred)}
    # asyncio.run(predict(features))  # type: ignore
