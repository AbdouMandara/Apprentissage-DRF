import requests

# POur recuperer tous les produits
endpoint_api = 'http://localhost:8000/api/product/'

# POur recuperer un produit (ex : 2)
endpoint_api_detail = 'http://localhost:8000/api/product/2'
response = requests.get(endpoint_api)

print(response.json())
print(response.status_code)