from .pokemon import Pokemon
from .utils import remove_empty_items


def from_csv_row_to_entity(row) -> Pokemon:
    _, name, type1, type2, total, hp, attack, defense, speed_attack, speed_defense, speed, generation, legendary = row.values()
    types = [row.lower() for row in remove_empty_items([type1, type2])]
    pokemon = Pokemon(name, types, int(total), int(hp), int(attack), int(defense), int(
        speed_attack), int(speed_defense), int(speed), int(generation), legendary == 'True')
    return pokemon
