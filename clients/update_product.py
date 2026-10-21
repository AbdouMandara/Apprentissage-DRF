import requests
endpoint_api = 'http://localhost:8000/api/product/1/'

data_posted = {
    'nom' : 'Patate',
    'prix' : 150,
    'description' : 'La patate est amere !'
}

response = requests.patch(endpoint_api, data=data_posted)
print(response.status_code)