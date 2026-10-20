import json

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
    post_data = request.body
    headers = request.headers
    print(headers)
    print('---------------')
    print(post_data)

    data = json.loads(post_data) #Je fais ceci pour que ce qui est envoyer ne soit plus sous forme de byte donc sans le petit 'b' a coter donc les donnees sont sous fome de dictionnaire
    data['message'] = 'Reussi !'

    return JsonResponse(data) #Pour retourner les donnees soumisses lors de l'appel de l'api