"""
Le router sert à générer automatiquement les URLs associées à ton ModelViewSet
"""

from django.urls import path
from api.api.viewset import ProductViewSet
from rest_framework.routers import DefaultRouter, SimpleRouter

"""
DefaultRouter est utilise pour les operations CRUD
SimpleRouter est utilise pour les operations de lecture
"""

router = DefaultRouter()

# Pour tester je vais me rendre sur : http://localhost:8000/api/v1/product/
router.register('v1/product', ProductViewSet, basename='product')

urlpatterns = router.urls