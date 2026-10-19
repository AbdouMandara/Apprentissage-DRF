# Pour tester ca je fais juste : python test.py aprs avoir lancer le serveur en faisant = python manage.py runserver
import requests

endpoint = 'http://localhost:8000/api/?nom=AbdouMandara'

# C'est pour faire un get sur mon endpoint et recuperer la reponse
response = requests.get(endpoint)

# J'affiche la reponse en JSON
print(response.json())

# Affichage du status code de la requete
print(response.status_code)
