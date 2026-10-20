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
    post_data = request.POST
    headers = request.headers
    print(headers)
    print(post_data)
    return JsonResponse({
        'message' : 'Creation reussi',
    })