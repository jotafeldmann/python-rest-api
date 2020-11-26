import argparse

from importer import csv
from pokemons.csv import from_csv_row_to_entity
from pokemons.rules import is_excluded, adjust_skills
from api import api
from data import data
from logger import logger


def input_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Pokemon API')
    parser.add_argument('file', type=str, help='the .csv input file')
    parser.add_argument('--port', type=str, help='API port', default=8000)
    args = parser.parse_args()
    return args


def import_data(file):
    logger.info('CSV import: starting')

    total_rows = 0
    imported_rows = 0
    records = []

    for row in csv.parse(file, skip_header=False):
        total_rows = total_rows + 1
        pokemon = from_csv_row_to_entity(row)

        if is_excluded(pokemon):
            continue

        imported_rows = imported_rows + 1
        pokemon = adjust_skills(pokemon)
        records.append(pokemon)

    logger.info('CSV import: imported {}/{} rows'.format(
        imported_rows, total_rows))

    return records


def main(args):
    logger.info('App: starting')
    records = import_data(args.file)
    logger.info('Data: starting')
    data.create(records)
    logger.info('Data: started')
    logger.info('API: running at port {}'.format(args.port))
    return api.start(args)


if __name__ == "__main__":
    main(args=input_arguments())
