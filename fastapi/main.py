from fastapi import FastAPI
from routers import aiModelRealEstatePredictor  # type: ignore
import pickle
import asyncio


app = FastAPI()

model = pickle.load(
    open("/Users/trentcain/ML-Project-phData/model/model.pkl", "rb"))


app.include_router(aiModelRealEstatePredictor.router)
