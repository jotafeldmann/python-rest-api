from src.main import import_data
from src.importer import csv
from src.pokemons.csv import from_csv_row_to_entity

from tests import file_path

all_rows = []
for row in csv.parse(file_path, skip_header=False):
    all_rows.append(from_csv_row_to_entity(row))


def test_main():
    adjusted_rows = []
    for row in import_data(file_path):
        adjusted_rows.append(row)

    assert len(all_rows) != len(adjusted_rows)
