from fastapi import FastAPI

from routers import aiModelRealEstatePredictor, authenticate
import pickle
from .database import engine


description = """
With the Real-Estate House Predictor App, you can locate pinpoint pricing for your next client engagment
#######

This is an amazing opportunity to leverage enormous insights over out competitors, and further stablize relationships with
our customers

With the use of Machine Learning, we can deploy rapid scalibity of our API that, that provides seemless predictions
"""
app = FastAPI(title="Real Estate Pricing Predictor ML Model",
              description=description,
              summary="There are some humongous houses in the US. Lets determine the price",
              version="0.0.1",
              terms_of_service="https://www.phdata.io/legal/website-terms-of-use/",
              contact={
                  "name": "phData",
                  "url": "https://www.phdata.io/about-us/",
                  "email": "trent.cain@phdata.blah",
              },
              license_info={
                  "name": "OpenAI",
                  "url": "https://openai.com/",
              },
              )


model_artifact = pickle.load(
    open("/Users/trentcain/ML-Project-phData/model/model.pkl", "rb"))

model.Base.metadata.create_all(bind=engine)
app.include_router(aiModelRealEstatePredictor.router)
app.include_router(authenticate.router)
