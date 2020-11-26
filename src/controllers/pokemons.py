from functools import partial

from pokemons.pokemon import Pokemon
from data import data
from .utils import generate_parameters_modifiers, predicate

schema = {k: v for k, v in Pokemon.__annotations__.items()}
parameters_schema = generate_parameters_modifiers(schema)
parameters = [k for k in parameters_schema.keys()]


def get_by_id(id: int) -> Pokemon:
    return data.get(id)


def search(page: int, items_per_page: int, search=None):
    p = None

    if search:
        p = partial(predicate, parameters_schema, search)

    records, records_in_page, page, total_pages, records_per_page, total_records = data.search(
        page=page, records_per_page=items_per_page, predicate=p)
    return records, records_in_page, page, total_pages, records_per_page, total_records


def get_parameters():
    return parameters
