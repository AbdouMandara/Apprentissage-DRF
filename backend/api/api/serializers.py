# LEs serializer sont comme les formulaires dans Django donc on peut definir les champs d'un serializer ou encore faire le notre baser sur un model preexistant
from api.models import Product
from rest_framework import serializers
"""
Un serializer est un outil qui définit comment les données doivent être représentées, lues et validées lors des échanges avec ton API.
En gros, il est l'intermediaire entre Django et le front-end.
"""

#Serializer baser sur un model
class ProductSerializer(serializers.ModelSerializer):
    class Meta :
        model = Product #Pour dire le model sur lequel je me base
        fields = '__all__' #Pour definir tous les champs exposes par l'api
        read_only_fields = ['created_at', 'updated_at'] #Ca dit les champs que le client ne pourra pas modifer s'il s'agit d'un POST neamoins ca peut etre retourne

#Serializer baser sans model
class ProductSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=255)
    prix = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()

