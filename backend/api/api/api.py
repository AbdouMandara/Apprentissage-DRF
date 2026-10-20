
from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#Comment developper une api rest avec le decorateur api_view

@api_view(['GET', 'POST'])

def product_api_view(request):
    if request.method == 'GET' :
        products = Product.objects.all()
        data = [{
            'id' : product.id,
            'nom' : product.nom
        } for product in products]