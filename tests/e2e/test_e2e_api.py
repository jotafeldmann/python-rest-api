from tests import file_path
import json
from tornado.testing import AsyncHTTPTestCase

from api.api import api
from main import import_data, data
from tests import file_path

records = import_data(file_path)
data.create(records)


class TestApi(AsyncHTTPTestCase):
    def get_app(self):
        return api()

    def test_get_all(self):
        response = self.fetch('/pokemons', method="GET")
        assert response.code == 200

        body_json = json.loads(response.body)
        assert body_json.get('items') == 20
        assert body_json.get('page') == 1
        assert body_json.get('total_pages') == 35
        assert body_json.get('items_per_page') == 20
        assert body_json.get('total_items') == 692
        assert body_json.get('data') != None

    def test_get_one(self):
        response = self.fetch('/pokemons/0', method="GET")
        assert response.code == 200

        body_json = json.loads(response.body)
        assert body_json == {'name': 'Bulbasaur', 'total': 318, 'hp': 45, 'attack': 49, 'defense': 49, 'speed_attack': 65,
                             'speed_defense': 65, 'speed': 45, 'generation': 1, 'legendary': False, 'types': {'grass': True, 'poison': True}}

    def test_get_one_not_found(self):
        response = self.fetch('/pokemons/999', method="GET")
        assert response.code == 404

        body_json = json.loads(response.body)
        assert body_json == {'error': 'Not found'}

    def test_get_all_filter_by_purpose_example(self):
        response = self.fetch(
            '/pokemons?hp[gte]=100&defense[lte]=200', method="GET")
        assert response.code == 200

        body_json = json.loads(response.body)
        assert body_json.get('items') == 20
        assert body_json.get('page') == 1
        assert body_json.get('total_pages') == 5
        assert body_json.get('items_per_page') == 20
        assert body_json.get('total_items') == 97
        assert len(body_json.get('data')) == 20

    def test_get_all_filter_by_hp_name(self):
        response = self.fetch(
            '/pokemons?items_per_page=3&hp[gte]=100&name[like]=mag', method="GET")
        assert response.code == 200

        body_json = json.loads(response.body)
        assert body_json.get('items') == 3
        assert body_json.get('page') == 1
        assert body_json.get('total_pages') == 2
        assert body_json.get('items_per_page') == 3
        assert body_json.get('total_items') == 4
        assert len(body_json.get('data')) == 3

    def test_get_all_filter_by_exact_name(self):
        response = self.fetch(
            '/pokemons?name=magneton', method="GET")
        assert response.code == 200

        body_json = json.loads(response.body)
        assert body_json.get('items') == 1
        assert body_json.get('page') == 1
        assert body_json.get('total_pages') == 1
        assert body_json.get('items_per_page') == 20
        assert body_json.get('total_items') == 1
        assert len(body_json.get('data')) == 1

    def test_get_all_filter_by_types(self):
        response = self.fetch(
            '/pokemons?types=fire', method="GET")
        assert response.code == 200

        body_json = json.loads(response.body)
        assert body_json.get('items') == 20
        assert body_json.get('page') == 1
        assert body_json.get('total_pages') == 3
        assert body_json.get('items_per_page') == 20
        assert body_json.get('total_items') == 53
        assert len(body_json.get('data')) == 20

        assert body_json.get('data')[0].get('types') == {'fire': True}
        assert body_json.get('data')[1].get('types') == {'fire': True}
        assert body_json.get('data')[2].get('types') == {
            'fire': True, 'flying': True}
        assert body_json.get('data')[3].get('types') == {
            'dragon': True, 'fire': True}
        assert body_json.get('data')[4].get('types') == {
            'fire': True, 'flying': True}
        assert body_json.get('data')[19].get('types') == {
            'dark': True, 'fire': True}

    def test_get_all_filter_by_a_type_and_or_another(self):
        response = self.fetch(
            '/pokemons?types=fire,ice', method="GET")
        assert response.code == 200

        body_json = json.loads(response.body)
        assert body_json.get('items') == 20
        assert body_json.get('page') == 1
        assert body_json.get('total_pages') == 5
        assert body_json.get('items_per_page') == 20
        assert body_json.get('total_items') == 85
        assert len(body_json.get('data')) == 20

        assert body_json.get('data')[0].get('types') == {'fire': True}
        assert body_json.get('data')[12].get('types') == {
            'ice': True, 'water': True}

    def test_get_all_filter_by_a_type_or_another(self):
        response = self.fetch(
            '/pokemons?types[or]=fire,ice', method="GET")
        assert response.code == 200

        body_json = json.loads(response.body)
        assert body_json.get('items') == 20
        assert body_json.get('page') == 1
        assert body_json.get('total_pages') == 2
        assert body_json.get('items_per_page') == 20
        assert body_json.get('total_items') == 39
        assert len(body_json.get('data')) == 20

        assert body_json.get('data')[0].get('types') == {'fire': True}
        assert body_json.get('data')[12].get('types') == {'fire': True}

    def test_get_all_filter_by_all_types(self):
        response = self.fetch(
            '/pokemons?types[all]=fire,electric', method="GET")
        assert response.code == 200

        body_json = json.loads(response.body)
        assert body_json.get('items') == 1
        assert body_json.get('page') == 1
        assert body_json.get('total_pages') == 1
        assert body_json.get('items_per_page') == 20
        assert body_json.get('total_items') == 1
        assert len(body_json.get('data')) == 1

        assert body_json.get('data')[0].get('types') == {
            'electric': True, 'fire': True}

    def test_get_all_filter_by_levenshtein_distance(self):
        response = self.fetch(
            '/pokemons?name[like]=meow', method="GET")
        assert response.code == 200

        body_json = json.loads(response.body)
        assert body_json.get('items') == 5
        assert body_json.get('page') == 1
        assert body_json.get('total_pages') == 1
        assert body_json.get('items_per_page') == 20
        assert body_json.get('total_items') == 5
        assert len(body_json.get('data')) == 5

        assert body_json.get('data')[0].get('name') == 'Meowth'
        assert body_json.get('data')[1].get('name') == 'Mew'
        assert body_json.get('data')[2].get('name') == 'Glameow'
        assert body_json.get('data')[3].get('name') == 'MeowsticMale'
        assert body_json.get('data')[4].get('name') == 'MeowsticFemale'

    def test_get_all_pagination(self):
        response = self.fetch(
            '/pokemons?items_per_page=1&page=2', method="GET")
        assert response.code == 200

        body_json = json.loads(response.body)
        assert body_json.get('items') == 1
        assert body_json.get('page') == 2
        assert body_json.get('total_pages') == 692
        assert body_json.get('items_per_page') == 1
        assert body_json.get('total_items') == 692
        assert len(body_json.get('data')) == 1
