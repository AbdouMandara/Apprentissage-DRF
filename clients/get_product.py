import requests

endpoint_api = 'http://localhost:8000/api/product/'

response = requests.get(endpoint_api)

print(response.json())
print(response.status_code)