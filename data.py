import requests


parameters = {
    "amount":10,
    "type": "boolean",
    "category":18
}
result = requests.get("https://opentdb.com/api.php",params=parameters)
data = result.json()
question_data = data["results"]

# print(question_data)
