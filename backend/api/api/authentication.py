from rest_framework.authentication import TokenAuthentication


class TokenAuthenticationCustom(TokenAuthentication):
    """
    Ce code sert à personnaliser la manière dont DRF attend le token dans l’en-tête HTTP
    Par défaut, le client envoie => Authorization : Token
    Avec keyword modifier ca sera maintenant 
    Authorization : Bearer

    Ca peut servir a cause de la securite
    """

    keyword = 'Bearer'