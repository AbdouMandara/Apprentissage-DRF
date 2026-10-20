# LEs serializer sont comme les formulaires dans Django donc on peut definir les champs d'un serializer ou encore faire le notre baser sur un model preexistant
from api.models import Product
from rest_framework import serializers
"""
Un serializer est un outil qui définit comment les données doivent être représentées, lues et validées lors des échanges avec ton API.
En gros, il est l'intermediaire entre Django et le front-end.
"""

class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product #Pour dire le model sur lequel je me base
        fields = '__all__' #Pour definir tous les champs exposes par l'api