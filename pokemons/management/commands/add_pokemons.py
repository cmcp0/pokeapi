from typing import List
from unicodedata import name
from django.core.management.base import BaseCommand, CommandError
from pokemons.models import *
from pokemons.utils.api_request import(
    ApiRequest,
    GetEvolutionChain,
    GetPokemonData
)

class Command(BaseCommand):
    help = 'Add the evolution-chains\'s pokemon'
    getEvolutionChainClient: ApiRequest
    getPokemonData: ApiRequest
    stats_map = {
        'hp': Hp,
        'attack': Attack,
        'defense': Defense,
        'special-attack': SpecialAttack,
        'special-defense': SpecialDefense,
        'speed': Speed
    }

    def add_arguments(self, parser):
        parser.add_argument('id', type=int)

    def handle(self, *args, **options):
        if options['id'] is None:
            raise CommandError('Must provide evolution-chain id')
        self.getEvolutionChainClient = GetEvolutionChain()
        self.getPokemonDataClient = GetPokemonData()
        try:
            chain = self.getEvolutionChainClient.get(options['id'])
            
            pokemons = self.mapPokemonChain(chain['chain'], None)
            self.stdout.write(f"pokemons {pokemons}", ending='\n')
        except Exception as error:
            raise CommandError(error)

    def mapPokemonChain(self, pokemon: dict, pre_evolution: Pokemon) -> dict:
        self.stdout.write(f".", ending='')

        mapped_pokemon = Pokemon(
            id= int(pokemon['species']['url'].split('/')[-2]),
            name= pokemon['species']['name']
        )

        pokemon_info = self.getPokemonDataClient.get(mapped_pokemon.id)
        mapped_pokemon.height = pokemon_info['height']
        mapped_pokemon.weight = pokemon_info['weight']
        mapped_pokemon.save()

        stats = map(
            lambda stat: self.createStat(stat, mapped_pokemon),
            pokemon_info['stats']
        )

        pokemon_preevolution = None
        if pre_evolution is not None:
            pokemon_preevolution = PreEvolution(
                key= mapped_pokemon,
                id_pokemon= pre_evolution.id,
                name_pokemon= pre_evolution.name
            )
            pokemon_preevolution.save()
        
        evolutions = map(
            lambda ev_pokemon: self.createEvolution(ev_pokemon, mapped_pokemon),
            pokemon['evolves_to']
        )

        return {            
            'pokemon': mapped_pokemon,
            'stats': list(stats),
            'pre_evolution': pokemon_preevolution,
            'evolutions': list(evolutions)
        }

    def createStat(self, stat: dict, pokemon: Pokemon) -> BaseStat:
        self.stdout.write(f"..", ending='')

        model: BaseStat = self.stats_map[stat['stat']['name']]
        mstat = model(
            pokemon= pokemon,
            name= stat['stat']['name'],
            stat= stat['base_stat'],
            effort= stat['effort']
        )
        mstat.save()
        return mstat
    
    def createEvolution(self, pokemon: dict, pre_evolution: Pokemon) -> Evolution:
        self.stdout.write(f"...", ending='')

        mapped_pokemon = self.mapPokemonChain(pokemon= pokemon, pre_evolution= pre_evolution)
        
        evolution = Evolution(
            key= pre_evolution,
            id_pokemon= mapped_pokemon['pokemon'].id,
            name_pokemon= mapped_pokemon['pokemon'].name
        )
        evolution.save()
        return evolution
