import requests

BASE_URL = 'https://reqres.in/api'

query_params = {
    "page": 1
}

def callMeAgain(query_params):
	response = requests.get(f"{BASE_URL}/users", params=query_params)
	print(response.json())
	return response

callMeAgain(query_params)
print("calling rest_caller_2")
