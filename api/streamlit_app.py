import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # your FastAPI backend

st.set_page_config(page_title="Titanic Survival Prediction", page_icon="🚢", layout="centered")

st.title("🚢 Titanic Survival Prediction Dashboard")
st.markdown("Choose **Raw Input** if you want to enter passenger details. Or, use **Processed Input** if you already have engineered features.")
# Choice of input type
input_type = st.selectbox(
    "Choose input type:",
    ["Raw Input", "Processed Features"]
)

st.write("---")

if input_type == "Raw Input":
    st.subheader("Enter Passenger Details (Raw Schema)")

    passenger_data = {
        "PassengerId": st.text_input("Passenger ID (optional)"),
        "Pclass": st.selectbox("Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3]),
        "Name": st.text_input("Name (optional)"),
        "Sex": st.selectbox("Sex", ["male", "female"]),
        "Age": st.number_input("Age", min_value=0, step=1),
        "SibSp": st.number_input("Siblings/Spouses Aboard", min_value=0, step=1),
        "Parch": st.number_input("Parents/Children Aboard", min_value=0, step=1),
        "Ticket": st.text_input("Ticket (optional)"),
        "Fare": st.number_input("Fare", min_value=0.0, step=0.5),
        "Cabin": st.text_input("Cabin (optional)"),
        "Embarked": st.selectbox("Embarked", ["C", "Q", "S"]),
    }

    if st.button("Predict from Raw Data"):
        with st.spinner("Contacting model..."):
            try:
                response = requests.post(f"{API_URL}/predict", json=passenger_data)
                if response.status_code == 200:
                    result = response.json()
                    st.success(f"✅ Prediction: {result['prediction']}, Survival Probability: {result['probability_of_survival']}")
                else:
                    st.error(f"❌ Error: {response.text}")
            except Exception as e:
                st.error(f"⚠️ Could not connect to API: {e}")


elif input_type == "Processed Features":
    st.subheader("Enter Preprocessed Passenger Features")

    processed_data = {
        "Pclass": st.selectbox("Class (1, 2, 3)", [1, 2, 3]),
        "Sex_male": st.selectbox("Sex_male (1=Male, 0=Female)", [0, 1]),
        "Age_Bin": st.number_input("Age_Bin", min_value=0, step=1),
        "Family_Group": st.number_input("Family_Group", min_value=0, step=1),
        "Fare_Bin": st.selectbox("Fare_Bin (0=Low,1=Mid,2=High,3=Very High)", [0, 1, 2, 3]),
        "Embarked_Q": st.selectbox("Embarked_Q (1=Yes,0=No)", [0, 1]),
        "Embarked_S": st.selectbox("Embarked_S (1=Yes,0=No)", [0, 1]),
    }

    if st.button("Predict from Processed Features"):
        with st.spinner("Contacting model..."):
            try:
                response = requests.post(f"{API_URL}/predict_processed", json=processed_data)
                if response.status_code == 200:
                    result = response.json()
                    st.success(f"✅ Prediction: {result['prediction']}, Survival Probability: {result['probability_of_survival']}")
                else:
                    st.error(f"❌ Error: {response.text}")
            except Exception as e:
                st.error(f"⚠️ Could not connect to API: {e}")
