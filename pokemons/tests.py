from django.test import TestCase

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
    