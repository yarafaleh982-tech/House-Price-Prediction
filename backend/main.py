from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pandas as pd
import joblib
import json

app = FastAPI(title="House Price Prediction API")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained model
model = joblib.load("house_price.pkl")

# Load locations
with open("locations.json", "r") as f:
    locations = json.load(f)


# Input schema
class House(BaseModel):
    carpet_area_sqft: float
    floor_num: float
    Bathroom: float
    Balcony: float
    location_grouped: str
    Furnishing: str
    Transaction: str
    Ownership: str
    facing: str


# Home API
@app.get("/")
def home():
    return {"message": "House Price Prediction API is Running"}


# Get all locations
@app.get("/locations")
def get_locations():
    return locations


# Predict price
@app.post("/predict")
def predict(data: House):

    sample = pd.DataFrame([{
        "carpet_area_sqft": data.carpet_area_sqft,
        "floor_num": data.floor_num,
        "Bathroom": data.Bathroom,
        "Balcony": data.Balcony,
        "location_grouped": data.location_grouped,
        "Furnishing": data.Furnishing,
        "Transaction": data.Transaction,
        "Ownership": data.Ownership,
        "facing": data.facing
    }])

    prediction = model.predict(sample)[0]

    return {
        "Predicted Price": float(prediction)
    }