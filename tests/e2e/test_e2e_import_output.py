import json
from tests import file_path
from src.main import import_data

tests_folder = './tests/e2e'
test_e2e_import_output_expected_file = '{}/test_e2e_import_output_expected.txt'.format(
    tests_folder)
test_e2e_import_output_generated_file = '{}/test_e2e_import_output_generated.txt'.format(
    tests_folder)

with open(test_e2e_import_output_expected_file, "r") as file:
    test_e2e_output_expected = file.read()


def test_e2e_generated_output():
    records = import_data(file=file_path)
    assert len(records) == 692

    records_json = json.dumps(
        [row.__dict__ for row in records], sort_keys=True, indent=2)

    with open(test_e2e_import_output_generated_file, "w") as file:
        file.write(records_json)
        file.close()

    assert (records_json) == test_e2e_output_expected
