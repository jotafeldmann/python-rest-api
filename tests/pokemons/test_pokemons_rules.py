from src.pokemons.rules import adjust_skills, is_excluded
from src.pokemons.pokemon import Pokemon
from tests.fixtures.pokemon import any_pokemon

common_pokemon = any_pokemon()

pokemon_excluded_ghost = any_pokemon()
pokemon_excluded_ghost.types['ghost'] = True

pokemon_excluded_legendary = any_pokemon()
pokemon_excluded_legendary.legendary = True


def test_rules_is_excluded():
    assert is_excluded(pokemon_excluded_ghost) == True
    assert is_excluded(common_pokemon) == False
    assert is_excluded(pokemon_excluded_legendary) == True


def test_rules_adjust_skills():
    pokemon = any_pokemon()
    pokemon.types['steel'] = True
    pokemon.hp = 100
    assert adjust_skills(pokemon).hp == 200

    pokemon = any_pokemon()
    pokemon.types['fire'] = True
    pokemon.attack = 1
    # Should not be less than 1
    assert adjust_skills(pokemon).attack == 1

    pokemon = any_pokemon()
    pokemon.types['fire'] = True
    pokemon.attack = 99
    assert adjust_skills(pokemon).attack == 90

    pokemon = any_pokemon()
    pokemon.types['flying'] = True
    pokemon.speed_attack = 50
    assert adjust_skills(pokemon).speed_attack == 55

    pokemon = any_pokemon()
    pokemon.types['bug'] = True
    pokemon.speed_attack = 2
    # Any increase must be meaningful for an integer
    assert adjust_skills(pokemon).speed_attack == 3

    pokemon = any_pokemon()
    pokemon.types['bug'] = True
    pokemon.types['fire'] = True
    pokemon.speed_attack = 10
    assert adjust_skills(pokemon).speed_attack == 11

    pokemon = any_pokemon()
    pokemon.name = 'Gorgorog'
    pokemon.defense = 10
    assert adjust_skills(pokemon).defense == 35

    pokemon = any_pokemon()
    before = pokemon.__str__()
    assert adjust_skills(pokemon).__str__() == before
