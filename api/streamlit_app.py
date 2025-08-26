import streamlit as st
import requests

st.set_page_config(page_title="Titanic Survival Predictor", layout="centered")

st.title("🚢 Titanic Survival Prediction")
st.write("Enter passenger details to predict survival probability.")

# Choose raw vs processed
option = st.radio("Select Input Type:", ["Raw Passenger Data", "Processed Features"])

if option == "Raw Passenger Data":
    st.subheader("Raw Passenger Data")
    Pclass = st.selectbox("Passenger Class (1 = Upper, 2 = Middle, 3 = Lower)", [1, 2, 3])
    Sex = st.selectbox("Sex", ["male", "female"])
    Age = st.slider("Age", 0, 80, 25)
    SibSp = st.number_input("Number of Siblings/Spouses aboard", 0, 8, 0)
    Parch = st.number_input("Number of Parents/Children aboard", 0, 6, 0)
    Fare = st.number_input("Fare", 0.0, 500.0, 32.0)
    Embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

    if st.button("Predict"):
        payload = {
            "Pclass": Pclass,
            "Sex": Sex,
            "Age": Age,
            "SibSp": SibSp,
            "Parch": Parch,
            "Fare": Fare,
            "Embarked": Embarked
        }
        res = requests.post("http://127.0.0.1:8000/predict", json=payload)  # FastAPI raw endpoint
        st.write(res.json())

else:
    st.subheader("Processed Passenger Features")
    Pclass = st.selectbox("Passenger Class", [1, 2, 3])
    Sex_male = st.selectbox("Is Male?", [0, 1])
    Embarked_Q = st.selectbox("Embarked at Q?", [0, 1])
    Embarked_S = st.selectbox("Embarked at S?", [0, 1])
    Fare_Bin = st.selectbox("Fare Bin", [0, 1, 2, 3])
    Age_Bin = st.selectbox("Age Bin", [0, 1, 2, 3])
    Family_Group = st.selectbox("Family Group", [0, 1, 2])

    if st.button("Predict"):
        payload = {
            "Pclass": Pclass,
            "Sex_male": Sex_male,
            "Embarked_Q": Embarked_Q,
            "Embarked_S": Embarked_S,
            "Fare_Bin": Fare_Bin,
            "Age_Bin": Age_Bin,
            "Family_Group": Family_Group
        }
        res = requests.post("http://127.0.0.1:8000/predict_processed", json=payload)
        st.write(res.json())
