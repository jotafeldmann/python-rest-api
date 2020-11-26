from tornado import httpserver, ioloop, web

from api.controllers.pokemons import PokemonHandler


def api() -> web.Application:
    return web.Application(
        [(endpoint, PokemonHandler) for endpoint in PokemonHandler.endpoints])


def start(args):
    application = api()
    http_server = httpserver.HTTPServer(application)
    http_server.listen(args.port, '0.0.0.0')
    ioloop.IOLoop.current().start()
