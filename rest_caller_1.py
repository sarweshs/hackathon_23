import requests

BASE_URL = 'https://fakestoreapi.com'

query_params = {
    "limit": 3
}

def callMe(query_params):
	response = requests.get(f"{BASE_URL}/products", params=query_params)
	print(response.json())
	return response.json()

#callMe(query_params)
print("calling rest_caller_1")
