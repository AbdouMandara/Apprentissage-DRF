import requests

endpoint = 'http://localhost:8000/api/create'

data_posted = {
    'nom' : 'Mangue',
    'prix' : 250,
    'description' : 'La mangue est bonne , youpiiiiiii !'
}

# Je mets "json" lorsque ce que j'envoie doit etre en JSON (Cas de auth),
# Je mets "data" losque j'envoie des foms html nomaux, images 
response = requests.post(endpoint, json=data_posted)

# Cas : losque je veux faire une requete en GET
#response = requests.get(endpoint)
print(response.json())
print(response.status_code)