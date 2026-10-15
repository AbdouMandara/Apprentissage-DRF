from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({
        'message': 'Je retourne un message JSON depuis Django',
        'name' : 'Abdou',
        'age' : 25
    })