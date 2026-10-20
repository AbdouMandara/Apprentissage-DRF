import json
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    headers = request.headers
    params = request.GET
    params_nom = params.get('nom')

    post_data = request.POST
    print(headers)
    print('---------')
    print(post_data)
    return JsonResponse({
        'message': 'Je retourne un message JSON depuis Django',
        'name' : params_nom,
        'age' : 25,
    })

# on l'utilise pour que celui qui veut acceder a l'api n;a pas besoin de fournir un cookie avant de communiquer avec cette api
@csrf_exempt
def create(request):
    headers = request.headers
    if request.method == 'POST' :
        post_data = request.body
        data = json.loads(post_data) #Je fais ceci pour que ce qui est envoyer ne soit plus sous forme de byte donc sans le petit 'b' a coter donc les donnees sont sous fome de dictionnaire
        
        #Recuperation de tout ce qui est envoye'
        name = data.get('nom')
        prix = data.get('prix')
        description = data.get('description')

        product = Product.objects.create(
            nom = name,
            prix = prix,
            description = description
        )

        return JsonResponse({
            'id' : product.id,
            'nom' : product.nom,
            'prix' : product.prix,
            'description' : product.description,
            'message' : 'reussi'
        }) #Pour retourner les donnees soumisses lors de l'appel de l'api

    # Au cas où on est pas en POST donc en GET on retoune tous les produits en BDD
    products = Product.objects.all()
    data = [{
        'id' : product.id,
        'name' : product.nom,
        'prix' : product.prix,
    } for product in products]
    return JsonResponse(data)