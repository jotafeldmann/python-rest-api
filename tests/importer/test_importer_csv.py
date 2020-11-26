from src.importer import csv
from tests import file_path


def test_csv_parse_without_header():
    file = [row for row in csv.parse(file_path)]
    assert len(file) == 799

    a, b, *_ = file[0]
    assert a == '#'
    assert b == 'Name'

    a, b, *_ = file[0].values()
    assert a == '2'
    assert b == 'Ivysaur'


def test_csv_parse_with_header():
    file = [row for row in csv.parse(file_path, False)]
    assert len(file) == 800

    a, b, *_ = file[0]
    assert a == '#'
    assert b == 'Name'

    a, b, *_ = file[0].values()
    assert a == '1'
    assert b == 'Bulbasaur'
