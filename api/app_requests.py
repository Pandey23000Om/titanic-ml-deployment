import requests

url = "http://127.0.0.1:8000/"
response = requests.get(url)
print(response.json())


url = "http://127.0.0.1:8000/predict"
payload = {
    "PassengerId": "1",
    "Pclass": 3,
    "Name": "John Doe",
    "Sex": "male",
    "Age": 22.0,
    "SibSp": 1,
    "Parch": 0,
    "Ticket": None,
    "Fare": 7.25,
    "Cabin": None,
    "Embarked": "S",
}
response = requests.post(url, json=payload)
print(response.json())


url = "http://127.0.0.1:8000/predict_processed"
payload = {
    "Pclass": 3,
    "Sex_male": 1,
    "Age_Bin": 1,
    "Family_Group": 1,
    "Fare_Bin": 0,
    "Embarked_Q": 0,
    "Embarked_S": 1,
}
response = requests.post(url, json=payload)
print(response.json())
