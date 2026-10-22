# Les serializer sont comme les formulaires dans Django donc on peut definir les champs d'un serializer ou encore faire le notre baser sur un model preexistant
from api.models import Product
from rest_framework import serializers
from django.contrib.auth.models import User

"""
Un serializer est un outil qui définit comment les données doivent être représentées, lues et validées lors des échanges avec ton API.
En gros, il est l'intermediaire entre Django et le front-end.
"""

# Mise en place du serializer pour le User
class UserSerializer(serializers.ModelSerializer):
    """produits_de_cet_auteur = serializers.PrimaryKeyRelatedField(
        many=True, 
        read_only=True, 
        source='product_set' #le nom de l'attribut que DRF doit utiliser pour récupérer les produits de ce user comme auteur est une fk dans Product
    )"""

    # Attribut pour avoir les produits que le user actuellement connecté a creer
    produits_de_cet_auteur = serializers.SerializerMethodField()
    class Meta :
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'produits_de_cet_auteur']

    # Recup des produits d'un client
    def get_produits_de_cet_auteur(self,obj):
        products = obj.product_set.all() # requete dans le sens inverse donc je recupere les produits lies a ce user
        return ProductSerializer2(products, many=True).data # J'utilise le 2e serializer afin de pas reutiliser le 1er ce qui serait une repetition (mdr)
    


#Serializer baser sur un model
class ProductSerializer(serializers.ModelSerializer):

    # Creation des attributs personnaliser que je peux retourner si je le souhaite
    prix_in_dollars = serializers.SerializerMethodField()
    description_normal = serializers.SerializerMethodField()
    detail_link = serializers.SerializerMethodField()
    auteur_du_produit = UserSerializer(read_only=True)
    class Meta :
        model = Product #Pour dire le model sur lequel je me base
        fields = '__all__' #Pour definir tous les champs exposes par l'api, et utiliser lors de la validation par rapport a ce qui est envoyé
        #fields = ['id', 'nom', 'description_normal', 'prix_in_dollars', 'detail_link']
        read_only_fields = ['created_at', 'updated_at'] #Ca dit les champs que le client ne pourra pas modifer s'il s'agit d'un POST neamoins ca peut etre retourner lors d'un GET

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
        return request.build_absolute_uri(f"/api/v1/product/{obj.id}/")
#Serializer baser sans model
class ProductSerializer2(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = ['nom', 'prix']
