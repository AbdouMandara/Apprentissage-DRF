# Les serializer sont comme les formulaires dans Django donc on peut definir les champs d'un serializer ou encore faire le notre baser sur un model preexistant
from api.models import Product
from rest_framework import serializers
"""
Un serializer est un outil qui définit comment les données doivent être représentées, lues et validées lors des échanges avec ton API.
En gros, il est l'intermediaire entre Django et le front-end.
"""

#Serializer baser sur un model
class ProductSerializer(serializers.ModelSerializer):
    prix_in_dollars = serializers.SerializerMethodField()
    description_normal = serializers.SerializerMethodField()
    detail_link = serializers.SerializerMethodField()
    class Meta :
        model = Product #Pour dire le model sur lequel je me base
        fields = '__all__' #Pour definir tous les champs exposes par l'api
        #fields = ['id', 'nom', 'description_normal', 'prix_in_dollars', 'detail_link']
        read_only_fields = ['created_at', 'updated_at'] #Ca dit les champs que le client ne pourra pas modifer s'il s'agit d'un POST neamoins ca peut etre retourne

    def validate_nom(self, value):
        if value.lower() == "test":
            raise serializers.ValidationError(
                "Ce nom n'est pas autorisé."
            )
        return value

    # Nous creons le user en passant a l'attribut 'auteur_du_produit' le user qui est connecte actuellement automatiquement
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['auteur_du_produit'] = user
        return super().create(validated_data)

    # Connexion des champs qui represente les valeurs renvoyes et les methodes depuis le model
    def get_prix_in_dollars(self, obj):
        return obj.get_prix_in_dollars()
    def get_description_normal(self, obj):
        return obj.get_description_normal()

    # Je relies mon attribut detail_link (pour avoir le lien qui mene au detail de ce produit) a l'attribut
    def get_detail_link(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return request.build_absolute_uri(f"/api/product/{obj.id}/")
    
#Serializer baser sans model
class ProductSerializer2(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=255)
    prix = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()

