import requests
from models.models import engine, Pokemon
from sqlalchemy.orm import sessionmaker
from typing import Any

# criando sessão para realizar as operações no BD
Session = sessionmaker(bind=engine)
local_session = Session()

# função que faz requisição GET dos dados do Pokemon e retorna o nome
def fetch_pokemon_data(pokemon_name: str) -> Any:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    response: requests.Response = requests.get(url=url)
    data: Any = response.json()
    return data['name']

pokemon_name: str = input('Informe o nome de um pokemon: ')

try:
    pokemon_data = fetch_pokemon_data(pokemon_name)
    pokemon: Pokemon = Pokemon(name=pokemon_data)
    local_session.add(pokemon)
    local_session.commit()
    print('Pokemon adicionado na tabela')
except Exception as e:
    print(f'err: {e}')