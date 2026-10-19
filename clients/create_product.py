import requests

endpoint = 'http://localhost:8000/api/create'

data_posted = {
    'nom' : 'Mangue',
    'prix' : 250,
    'description' : 'La mangue est bonne , youpiiiiiii !'
}

response = requests.post(endpoint, data=data_posted)
print(response.json)
print(response.status_code)