import json

from flask import Flask, abort

from .pokemon import (
    InvalidPokemonError,
    PokemonAPIError,
    get_pokemon_description,
)


EXAMPLE_RESPONSE = {
    "name": "charizard",
    "description": "pokemon description",
}


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config:
        app.config.update(test_config)

    @app.route("/<pokemon>")
    def hello(pokemon):
        try:
            description = get_pokemon_description(pokemon)
        except InvalidPokemonError:
            abort(404)
        except PokemonAPIError:
            # Something wrong with the API call that we don't know how to fix.
            abort(500)

        return {
            "name": pokemon,
            "description": description,
        }

    return app
