import csv
from typing import Iterator, Dict

Row = Dict[str, str]


def parse(file_path: str, skip_header: bool = True) -> Iterator[Row]:
    with open(file_path) as file:
        reader = csv.DictReader(file)

        if skip_header:
            next(reader, None)

        for row in reader:
            yield row
