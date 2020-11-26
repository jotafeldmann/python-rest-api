from src.pokemons.csv import from_csv_row_to_entity
from src.pokemons.pokemon import Pokemon
from src.importer import csv
from tests import file_path

rows = csv.parse(file_path)


def test_from_csv_row_to_entity():
    entities = []
    for row in rows:
        entities.append(from_csv_row_to_entity(row))

    assert isinstance(entities[0], Pokemon)
    assert entities[0].name == 'Ivysaur'
