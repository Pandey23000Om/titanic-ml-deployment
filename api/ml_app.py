from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
import joblib
import numpy as np

# Initialize FastAPI
app = FastAPI(title="Titanic Survival Prediction API")

# Load saved model once at startup
model = joblib.load("../model/svm_model.pkl")

# Define input schema (features according to the dataset)
class PassengerRaw(BaseModel):
    PassengerId: Optional[str]
    Pclass: int = Field(..., ge=1, le=3)   # must be 1,2,3
    Name: Optional[str]
    Sex: str
    Age: float = Field(..., ge=0)          # no negatives
    SibSp: int = Field(..., ge=0)
    Parch: int = Field(..., ge=0)
    Ticket: Optional[str]
    Fare: float = Field(..., ge=0)
    Cabin: Optional[str]
    Embarked: str = "S" # default value

# Function to preprocess raw input into model-ready features
def preprocess_input_data(passenger: PassengerRaw):
    # Encode Sex
    sex_male = 1 if passenger.Sex.lower() == "male" else 0

    # One-hot encoding for Embarked
    embarked = (passenger.Embarked or "").strip().upper()
    embarked_Q = 1 if embarked.upper() == "Q" else 0
    embarked_S = 1 if embarked.upper() == "S" else 0
    # C is dropped

    # Binning age
    if passenger.Age <= 12:
        age_bin = 0
    elif passenger.Age <=19:
        age_bin = 1
    elif passenger.Age <=35:
        age_bin = 2
    elif passenger.Age <=59:
        age_bin = 3
    else: age_bin=4
    
    # Binning fare
    if passenger.Fare <= 10:
        fare_bin = 0
    elif passenger.Fare <= 50:
        fare_bin = 1
    else: fare_bin = 2

    # Family Group
    family_size = passenger.SibSp + passenger.Parch

    return np.array([[
        passenger.Pclass, 
        sex_male, 
        embarked_Q, 
        embarked_S, 
        fare_bin, 
        age_bin, 
        family_size
        ]])


@app.get("/")
def root():
    return {"message": "Titanic Survival Prediction API is running! Open '/docs' to begin testing using swagger"}

@app.post("/predict")
def predict(passenger: PassengerRaw):
    # Preprocess the user input data
    features = preprocess_input_data(passenger)
    
    # Predict
    prediction = model.predict(features)[0]
    # return {"prediction": int(prediction), "survived": bool(prediction)}

    probability = model.predict_proba(features)[0][1]  # survival probability
    return {
        "prediction": int(prediction),
        "survived": bool(prediction),
        "probability_of_survival": float(probability)
    }
