from fastapi import FastAPI
from routers import aiModelRealEstatePredictor
import pickle

app = FastAPI()

model = pickle.load(open("/model/model.pkl", "rb"))

app.include_router(aiModelRealEstatePredictor.router)
