from django.urls import re_path
from pokemons import views

urlpatterns = [
    re_path('^pokemon', views.PokemonViewSet.as_view())
]
