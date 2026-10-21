from django.urls import path, include
from .views import home, create
from api.api.api import product_api_view

urlpatterns = [
    path('', home, name='home'),
    path('create', create, name='Creation'),
    path('product/', product_api_view, name='product_api_view'),
    path('product/<int:pk>/', product_api_view, name='product_api_view avec details'),
    path('', include('api.routers')),
]