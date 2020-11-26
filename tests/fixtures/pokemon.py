import copy
from src.pokemons.pokemon import Pokemon

_pokemon = Pokemon(
    'Xablau',
    ['Super', 'duper'],
    999,
    100,
    1,
    90,
    42,
    77,
    5,
    10,
    False
)


def any_pokemon():
    return copy.deepcopy(_pokemon)
