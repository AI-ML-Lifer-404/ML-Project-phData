from fastapi import APIRouter
from pydantic import BaseModel, Field
from starlette import status


router = APIRouter()


class RealEstatePricePredictor:
    id: int
    bedrooms: int
    bathrooms: float
    sqft_living: int
    sqft_lot: int
    floors: float
    waterfront: int
    view: int
    condition: int
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

    def __init__(self, id, bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, grade, sqft_above, sqft_basement, yr_built, yr_renovated, zipcode, lat, long, sqft_living15, sqft_lot15):
        self.id = id
        self.bedrooms = bedrooms
        self.sqft_living = sqft_living
        self.sqft_lot = sqft_lot
        self.floors = floors
        self.waterfront = waterfront
        self.view = view
        self.condition = condition
        self.grade = grade
        self.sqft_above = sqft_above
        self.sqft_basement
        self.yr_built = yr_built
        self.yr_renovated = yr_renovated
        self.zipcode = zipcode
        self.lat = lat
        self.long = long
        self.sqft_living15 = sqft_living15
        self.sqft_lot15 = sqft_lot15


class RealEstatePricePredictorRequest(BaseModel):
    bedrooms: int = Field(gt=0)
    bathrooms: float = Field(gt=0)
    sqft_living: int = Field(gt=0)
    sqft_lot: int = Field(gt=0)
    floors: float = Field(gt=0)
    waterfront: int = Field(gt=0)
    view: int = Field(gt=0)
    condition: int = Field(gt=0)
    grade: int = Field(gt=0)
    sqft_above: int = Field(gt=0)
    sqft_basement: int = Field(gt=0)
    yr_built: int = Field(gt=0)
    yr_renovated: int = Field(gt=0)
    zipcode: int = Field(gt=0)
    lat: float = Field(gt=0, lt=6)
    long: float = Field(gt=0, lt=6)
    sqft_living15: int = Field(gt=0)
    sqft_lot15: int = Field(gt=0)

    model_config = {
        "json_schema_extra": {
            "example": {
                "bedrooms": "Amount of bedrooms",
                "bathrooms": "Amount of bathrooms",
                "sqft_living": "Square footage of house",
                "sqft_lot": "Square footage of lot space",
                "floors": "The amount levels in the house",
                "waterfront": "Waterview view front or not (0 or 1)",
                "view": "City view or not",
                "condition": "The condition of the house",
                "grade": "Grade of house",
                "sqft_above": "Square foot above house",
                "sqft_basement": "Square footage of the basement",
                "yr_built": "The year that was built",
                "yr_renovated": "The year the house was renovated",
                "zipcode": "The zip code of the house",
                "lat": "The latitude",
                "long": "The longitude",
                "sqft_living15": "The square footage of the living room",
                "sqft_lot15": "The square footage of lot 15"
            }
        }
    }


class HousePrice(BaseModel):
    label: str
    prediction: int


@router.post("/predict")
async def get_home(features: RealEstatePricePredictorRequest, status_code=status.HTTP_200_OK):
    return {"message": features}
