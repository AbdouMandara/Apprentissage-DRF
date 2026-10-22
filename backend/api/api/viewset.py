from api.models import Product
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status
from api.api.serializers import ProductSerializer, ProductSerializer2
from rest_framework.decorators import action
from api.api.serializers import ProductSerializer, UserSerializer
from django.contrib.auth.models import User

# Api de User
class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ProductViewSet(ModelViewSet):
    # C'est comme les view dans Django ca ppermet de generer les routes CRUD pour ce model
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


    # Route personnalises 
    # Route pour les produits avec prix > 500
    @action(
        detail=False,
        methods=['GET'],
        url_path='expensive-product' #on pourra utiliser ca dans l'url ainsi pour acceder a cete route (ex : localhost:8000/api/v1/product/expensive-product)
    )
    def expensive_products(self, request, *args, **kwargs) :
        products = Product.objects.filter(prix__gte=500)
        context = {
            'request' : request
        } # on utilise request car ca nous sert au niveau de base_url au niveau du serializer
        serializer = ProductSerializer(products, many=True,context=context)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )