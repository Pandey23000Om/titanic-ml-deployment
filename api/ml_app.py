from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional
import joblib
# import numpy as np
import pandas as pd

# import warnings

# Initialize FastAPI
app = FastAPI(title="Titanic Survival Prediction API")

# Load saved model once at startup
model = joblib.load("../model/svm_model.pkl")

# Define input schema (features according to the raw dataset)
class PassengerRaw(BaseModel):
    PassengerId: Optional[str] = None
    Pclass: int = Field(..., ge=1, le=3)   # must be 1,2,3
    Name: Optional[str] = None
    Sex: str
    Age: float = Field(..., ge=0)          # no negatives
    SibSp: int = Field(..., ge=0)
    Parch: int = Field(..., ge=0)
    Ticket: Optional[str] = None
    Fare: float = Field(..., ge=0)
    Cabin: Optional[str] = None
    Embarked: str = "S" # default value

# Define input schema (features according to the model-ready dataset)
class PassengerProcessed(BaseModel):
    Pclass: int = Field(..., ge=1, le=3)        # must be 1,2,3
    Sex_male: int = Field(..., ge=0, le=1)  # must be 0 or 1
    Age_Bin: float = Field(..., ge=0)          # no negatives
    Family_Group: int = Field(..., ge=0)
    Fare_Bin: float = Field(..., ge=0, le=3)
    Embarked_Q: int = Field(..., ge=0, le=1)
    Embarked_S: int = Field(..., ge=0, le=1)

FEATURES = ["Pclass", "Sex_male", "Embarked_Q", "Embarked_S", "Fare_Bin", "Age_Bin", "Family_Group"]


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

    data = {
        "Pclass" : passenger.Pclass, 
        "Sex_male" : sex_male, 
        "Embarked_Q" : embarked_Q, 
        "Embarked_S" : embarked_S, 
        "Fare_Bin" : fare_bin, 
        "Age_Bin" : age_bin, 
        "Family_Group": family_size
    }
    return pd.DataFrame([data], columns=FEATURES)


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

@app.post("/predict_processed")
def predict_processed(passenger: PassengerProcessed):
    data = {
        "Pclass" : passenger.Pclass, 
        "Sex_male" : passenger.Sex_male, 
        "Embarked_Q" : passenger.Embarked_Q, 
        "Embarked_S" : passenger.Embarked_S, 
        "Fare_Bin" : passenger.Fare_Bin, 
        "Age_Bin" : passenger.Age_Bin, 
        "Family_Group": passenger.Family_Group
    }
    features = pd.DataFrame([data], columns=FEATURES)

    # Predict
    prediction = model.predict(features)[0]
    # return {"prediction": int(prediction), "survived": bool(prediction)}

    probability = model.predict_proba(features)[0][1]  # survival probability
    return {
        "prediction": int(prediction),
        "survived": bool(prediction),
        "probability_of_survival": float(probability)
    }
