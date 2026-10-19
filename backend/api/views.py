from django.http import JsonResponse

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