import requests
import os
from datetime import datetime

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
records_endpoint = os.getenv("SHEET_ENDPOINT")

exercise_text = input("Tell me which exercises you did: ")
gender = "female"
weight_kg = "54"
height_cm = "155"
age = "26"

headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
    "x-remote-user-id": "0"
}

parameters = {
    "query": exercise_text,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

response = requests.post(url=exercise_endpoint,json=parameters,headers=headers)
print(response.text)
exercises = response.json()["exercises"]

today = datetime.today()
for exercise in exercises:
    sheet_headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }
    body = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(records_endpoint, json=body, headers=sheet_headers)
    print(sheet_response.text)
