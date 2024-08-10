from fastapi import FastAPI
from routers import aiModelRealEstatePredictor


app = FastAPI()


app.include_router(aiModelRealEstatePredictor.router)
