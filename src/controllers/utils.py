import Levenshtein
import typing
import operator
from functools import partial

# https://en.wikipedia.org/wiki/Levenshtein_distance
RECOMENDED_LEVENSHTEIN_DISTANCE = 3


def search_by_insensitive_case(search, value):
    return search.lower() == value.lower()


def search_by_string_proximity(search, value):
    s = search.lower()
    v = value.lower()
    if search_by_insensitive_case(s, v):
        return True

    if s in v or v in s:
        return True

    distance = Levenshtein.distance(s, v)
    return distance < RECOMENDED_LEVENSHTEIN_DISTANCE


def search_by_bool(search, value):
    if not search.lower() in ['true', 'false']:
        return False

    predicate = search.lower() == 'true'

    return predicate == value


def search_by_type(comp, search, type):
    type_array = type.keys()
    array = search.split(',')
    if comp == 'full':
        return set(array) == set(type_array)

    comp = comp or any
    return comp(el in array for el in type_array)


def search_by_exact_value(search, value):
    return search == str(value)


def search_by_number(operator, search, number):
    return operator(number, int(search))


def add_searcher(key, searcher):
    return {
        'prop': key,
        'searcher': searcher
    }


def generate_parameters_modifiers(schema: dict):
    p = {}
    for k in schema:
        v = schema[k]

        if (v == int):
            p[k] = add_searcher(k, search_by_exact_value)
            p['{}[gt]'.format(k)] = add_searcher(
                k, partial(search_by_number, operator.gt))
            p['{}[gte]'.format(k)] = add_searcher(
                k, partial(search_by_number, operator.ge))
            p['{}[lt]'.format(k)] = add_searcher(
                k, partial(search_by_number, operator.lt))
            p['{}[lte]'.format(k)] = add_searcher(
                k, partial(search_by_number, operator.le))
            continue

        if (v == str):
            p[k] = add_searcher(k, search_by_insensitive_case)
            p['{}[like]'.format(k)] = add_searcher(
                k, search_by_string_proximity)
            continue

        if (v == bool):
            p[k] = add_searcher(k, search_by_bool)
            continue

        if (v == typing.Dict[str, bool]):
            p[k] = add_searcher(
                k, partial(search_by_type, any))
            p['{}[or]'.format(k)] = add_searcher(
                k, partial(search_by_type, all))
            p['{}[all]'.format(k)] = add_searcher(
                k, partial(search_by_type, 'full'))
            continue

        p[k] = add_searcher(k, search_by_exact_value)

    return p


def predicate(parameters_schema, search: dict, record):
    for k, v in search.items():
        real_k = parameters_schema[k]
        prop = real_k.get('prop')
        searcher = real_k.get('searcher')
        record_value = getattr(record, prop)

        if k in parameters_schema.keys():
            if not searcher(v, record_value):
                return False
            continue

        if not search_by_exact_value(v, record_value):
            return False

    return True
