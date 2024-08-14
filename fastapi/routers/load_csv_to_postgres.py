import json

from fastapi import FastAPI, UploadFile, File
from fastapi import APIRouter
from pydantic import BaseModel
from typing import Annotated
import pandas as pd
from starlette import status
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi import Depends, HTTPException, Path
import csv


router = APIRouter()


class FutureUnseenData(BaseModel):
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



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/upload/")
async def upload_csv(db: db_dependency, file: UploadFile = File):

    if not file.filename.endswith(".csv"):
        raise HTTPException(status=400, detail="Only CSV files are supported")

    content = await file.read()

    csv_data = content.decode("utf-8").splitlines()

    csv_reader = csv.reader(csv_data)

    for row in csv_reader:
        item = FutureUnseenData(bedrooms=row[0], bathrooms=row[1], sqft_living=row[2], sqft_lot=row[3], floors=row[4], waterfront=[5], view=[6], grade=[7], sqft_above=[8], sqft_basement=[9], yr_built=[10], yr_renovated=[11], zipcode=row[12], lat=row[13], long=row[14],sqft_living15=[15], sqft_lot15=row[16])
        print(item)
        db.add(item)

    db.commit()
    db.close()



