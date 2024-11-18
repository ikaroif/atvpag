from django.urls import path
from .views import listar_carros

urlpatterns = [
    path('', listar_carros, name='listar_carros'),
]
