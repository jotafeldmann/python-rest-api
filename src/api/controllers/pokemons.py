import json
from tornado.web import RequestHandler

from api.controllers.utils import safe_cast
from api.http_codes import HttpStatusCode
from controllers import pokemons


ITEMS_PER_PAGE = 20

RESPONSE_NOT_FOUND = (dict(error='Not found'), HttpStatusCode.NOT_FOUND.value)


class PokemonHandler(RequestHandler):

    search_parameters = pokemons.get_parameters()
    endpoints = [r'/pokemons/([0-9]+)?', r'/pokemons[/]?']

    def get(self, raw_id=None):
        if raw_id != None:
            body, code = self.get_by_id(raw_id)
        else:
            body, code = self.get_all()

        self.http_response(body, code)

    def get_all(self):
        page, items_per_page = self.get_pagination()
        search = self.get_query_parameters(self.search_parameters)

        records, records_in_page, page, total_pages, records_per_page, total_records = pokemons.search(
            page, items_per_page, search=search)
        body = [record.__dict__ for record in records]

        return dict(items=records_in_page, page=page, total_pages=total_pages, items_per_page=records_per_page, total_items=total_records, data=body), HttpStatusCode.OK.value

    def get_by_id(self, raw_id=None):
        _id = safe_cast(raw_id, int)

        if _id == None:
            return None, HttpStatusCode.BAD_REQUEST.value

        body = pokemons.get_by_id(_id)

        if body:
            return body.__dict__, HttpStatusCode.OK.value

        return RESPONSE_NOT_FOUND

    def get_query_parameters(self, parameters_list: list):
        parameters = {p: self.get_argument(p, None)
                      for p in parameters_list if self.get_argument(p, None)}
        return parameters

    def http_response(self, body=None, code=HttpStatusCode.OK.value):
        self._status_code = code
        if body == None:
            self.write('')
            return

        self.write(json.dumps(body))

    def set_default_headers(self):
        self.set_header('Content-Type', 'text/json')
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with')
        self.set_header('Access-Control-Allow-Methods', 'GET')

    def get_pagination(self):
        page = safe_cast(self.get_argument('page', '1'), int, 1)
        if page < 1:
            page = 1

        items_per_page = safe_cast(self.get_argument(
            'items_per_page', str(ITEMS_PER_PAGE)), int, ITEMS_PER_PAGE)

        if items_per_page < 1:
            items_per_page = ITEMS_PER_PAGE

        return page, items_per_page
