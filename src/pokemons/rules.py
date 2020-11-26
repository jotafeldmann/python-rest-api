import math
from .pokemon import Pokemon


def is_excluded(pokemon: Pokemon) -> bool:
    if pokemon.types.get('ghost') or pokemon.legendary:
        return True
    return False


def adjust_skills(pokemon: Pokemon) -> Pokemon:
    adjusted_pokemon = Pokemon(**pokemon.__dict__)

    if adjusted_pokemon.types.get('steel'):
        adjusted_pokemon.hp = adjusted_pokemon.hp * 2

    if adjusted_pokemon.types.get('fire'):
        adjusted_pokemon.attack = adjusted_pokemon.attack - math.floor(
            adjusted_pokemon.attack * 0.1)

    if adjusted_pokemon.types.get('bug') or adjusted_pokemon.types.get('flying'):
        adjusted_pokemon.speed_attack = adjusted_pokemon.speed_attack + math.ceil(
            adjusted_pokemon.speed_attack * 0.1)

    letter_to_check = 'g'
    if adjusted_pokemon.name[0].lower() == letter_to_check:
        for letter in adjusted_pokemon.name:
            if letter.lower() == letter_to_check:
                continue

            adjusted_pokemon.defense = adjusted_pokemon.defense + 5

    return adjusted_pokemon
