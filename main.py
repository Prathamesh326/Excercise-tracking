import requests
import datetime
import os

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
exercise_endpoint = os.environ['exercise_endpoint']
sheet_endpoint = os.environ['sheet_endpoint']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']

GENDER = "male"
WEIGHT_KG = 59
HEIGHT_CM = 167.64
AGE = 22

parameters = {
    'query': input("Tell me which exercises you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE

}

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

track_response = requests.post(exercise_endpoint, json=parameters, headers=headers)
track_api = track_response.json()

today = datetime.datetime.now()

for exercise in track_api['exercises']:
    workout_dict = {
        'workout':
            {
                'date': today.strftime("%d/%m/%Y"),
                'time': today.strftime("%X"),
                'exercise': exercise['name'].title(),
                'duration': exercise['duration_min'],
                'calories': exercise['nf_calories'],
            }
    }

    sheet_response = requests.post(sheet_endpoint, json=workout_dict, auth=(USER,PASSWORD))
    print(sheet_response.json())
