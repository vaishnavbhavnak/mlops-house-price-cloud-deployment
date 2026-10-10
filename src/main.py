import pickle
from pathlib import Path 
import logging
import pandas as pd 
from fastapi import FastAPI
from pydantic import BaseModel,Field

import os 
PORT= int(os.getenv("PORT","8001"))

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger(__name__)

BASE_DIR=Path(__file__).resolve().parent.parent
MODEL_PATH=BASE_DIR/"models"/"house_price_model.pkl"

with open(MODEL_PATH,"rb") as file:
    model=pickle.load(file)
    
app=FastAPI(
    title="House Price Prediction API",
    description="Predict house prices using a trained machine learning model",
    version="1.1.2"
)

class HouseFeatures(BaseModel):
    area: float =Field(gt=0,description="Area in square feet")
    bedrooms: int = Field(gt=0,le=20)
    age: int =Field(ge=0,le=200)
    
@app.get("/")
def home():
    return {
        "message":"House Price Prediction API is running"
    }
    
@app.get("/health")
def health():
    return {
        "status":"healthy"
    }
    
@app.post("/predict")
def predict_price(house:HouseFeatures):
    logger.info(
            "Prediction request receiver: area=%s, bedrooms=%s, age=%s",
            house.area,
            house.bedrooms,
            house.age 
        )
    input_data=pd.DataFrame(
        [[house.area,house.bedrooms,house.age]],
        columns=["area","bedrooms","age"]
    )
    
    prediction=model.predict(input_data)[0]
    
    return {
        "predicted_price_lakhs":round(float(prediction),2)
    }