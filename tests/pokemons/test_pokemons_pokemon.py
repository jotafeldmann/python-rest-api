from src.pokemons.pokemon import Pokemon
from tests.fixtures.pokemon import any_pokemon


def test_pokemon_entity():
    pokemon = any_pokemon()
    assert pokemon.__str__(
    ) == "Pokemon(name='Xablau', types={'Super': True, 'duper': True}, total=999, hp=100, attack=1, defense=90, speed_attack=42, speed_defense=77, speed=5, generation=10, legendary=False)"


def test_types_conversion():
    types = Pokemon.from_list_to_dict(['apple', 'banana', ''])

    assert types.__str__() == "{'apple': True, 'banana': True}"
    assert types.get('apple')
    assert types.get('banana') == True
