from django.test import TestCase
from django.core.management import call_command
from pokemons.models import Pokemon
from .utils.api_request import (
    ApiRequest,
    GetEvolutionChain,
    GetPokemonData
)

class ApiRequestTest(TestCase):
    evolution_chain_id: int
    pokemon_id: int
    getEvolutionChainClient: ApiRequest
    getPokemonDataClient: ApiRequest

    def setUp(self) -> None:
        self.evolution_chain_id = 1
        self.pokemon_id = 20
        self.getEvolutionChainClient = GetEvolutionChain()
        self.getPokemonDataClient = GetPokemonData()
        return super().setUp()

    def getEvolutionChainClientTest(self):
        chain = self.getEvolutionChainClient.get(self.evolution_chain_id)

        self.assertEqual(chain.id, self.evolution_chain_id)
        self.assertEqual(chain.chain.species.name, "bulbasaur")
    
    def getPokemonDataClientTest(self):
        pokemon = self.getPokemonDataClient.get(self.pokemon_id)

        self.assertEqual(pokemon.id, self.pokemon_id)
        self.assertEqual(pokemon.species.name, "raticate")
   
class AddPokemonsTest(TestCase):
    evolution_chain_id: int
    getEvolutionChainClient: ApiRequest

    def setUp(self) -> None:
        self.evolution_chain_id = 74

    def addPokemonsTest(self):
        chain = self.getEvolutionChainClient.get(self.evolution_chain_id)
        pokemon_id = chain['species']['url'].split('/')[-2]

        call_command('add_pokemons', options= self.evolution_chain_id)
        self.assertTrue(Pokemon.objects.filter(id= pokemon_id).exists)