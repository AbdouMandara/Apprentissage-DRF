
from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.api.serializers import ProductSerializer
#Comment developper une api rest avec le decorateur api_view

@api_view(['GET', 'POST'])

def product_api_view(request):
    if request.method == 'GET' :
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True) #many = True pour dire que cce que je t'envoie est plus d'un
        return Response(
            serializer.data, #C'est pour avoir acces au donnees
            status=status.HTTP_200_OK
        ) #C'est a Response que se passe la serialization
