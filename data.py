import requests

NUM_QUESTIONS = 10
QUESTION_TYPE = "boolean"

parameters = {
    "amount": NUM_QUESTIONS,
    "type": QUESTION_TYPE,
    "category": 18
}

question_data = []

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

for i in data['results']:
    question_data.append(i)



