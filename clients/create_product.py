import requests

endpoint = 'http://localhost:8000/api/create'
endpoint_api = 'http://localhost:8000/api/product/'

data_posted = {
    'nom' : 'Patate',
    'prix' : 400,
    'description' : 'La patate est delicieuse !'
}

# Je mets "json" lorsque ce que j'envoie doit etre en JSON (Cas de auth),
# Je mets "data" losque j'envoie des foms html nomaux, images 
response = requests.post(endpoint_api, json=data_posted)

# Cas : losque je veux faire une requete en GET
#response = requests.get(endpoint)
print(response.json())
print(response.status_code)