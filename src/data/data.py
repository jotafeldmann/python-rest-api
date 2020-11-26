# Due to time constraints this data structure will be in memory
import math
import re
from data.error import DataError


_records = []
_initialized = False
_len = 0


def create(records: list):
    global _initialized, _records, _len
    if _initialized:
        raise DataError('Data was already initialized')

    _records = records
    _initialized = True
    _len = len(_records)


def get(id):
    if id < 0 or id >= _len:
        return None

    return _records[id]


def search(page: int, records_per_page: int, predicate=None):
    results = []
    total_records = _len
    if predicate == None:
        results = _records
    else:
        for r in _records:
            if predicate(r):
                results.append(r)
        total_records = len(results)

    total_pages = math.ceil(total_records / records_per_page)
    start = (page - 1) * records_per_page
    end = start + (records_per_page)
    records = results[start:end]
    records_in_page = len(records)

    return records, records_in_page, page, total_pages, records_per_page, total_records
