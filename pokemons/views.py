from unicodedata import name
from pokemons.models import Pokemon

from pokemons.serializers import PokemonSerializer
from django.http import Http404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class PokemonViewSet(GenericAPIView):
    serialize_class = PokemonSerializer

    def get(self, request):
        try:
            pokemon_name = request.query_params.get('name')
            queryset = Pokemon.objects.get(name= pokemon_name)
            
            serializer = PokemonSerializer(queryset)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            raise Http404
