import requests

class ApiRequest():
    url: str

    def get(self, id: int) -> dict:
        pass

class GetEvolutionChain(ApiRequest):

    def __init__(self) -> None:
        super().__init__()
        self.url = 'https://pokeapi.co/api/v2/evolution-chain'

    def get(self, id: int) -> dict:
        try:
            response = requests.get(
                f'{self.url}/{id}'
            )
            return response.json()
        except Exception as error:
            raise error

class GetPokemonData(ApiRequest):

    def __init__(self) -> None:
        super().__init__()
        self.url = 'https://pokeapi.co/api/v2/pokemon'

    def get(self, id: int) -> dict:
        try:
            response = requests.get(
                f'{self.url}/{id}'
            )
            return response.json()
        except Exception as error:
            raise error