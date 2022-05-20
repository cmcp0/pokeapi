from numpy import source
from pokemons.models import (
    Pokemon,
    EvolutionType,
    BaseStat,
)

from rest_framework import serializers

class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseStat
        fields = [
            'name',
            'stat',
            'effort'
        ]

class EvolutionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvolutionType
        fields = [
            'type',
            'id_pokemon',
            'name_pokemon'
        ]

class PokemonSerializer(serializers.ModelSerializer):
    stats = StatSerializer(many=True, read_only=True, source= 'basestat_set')
    evolutions = EvolutionTypeSerializer(many=True, read_only=True, source= 'evolutiontype_set')

    class Meta:
        model = Pokemon
        fields = '__all__'