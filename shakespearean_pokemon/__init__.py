import json
from contextlib import contextmanager
from functools import wraps

from flask import Flask, abort

from .cache import get_cache
from .exceptions import InvalidPokemonError, TooManyRequestsError, UnknownAPIError
from .pokemon import get_pokemon_description
from .translate import TranslateAPIError, translate_to_shakespeare


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    if test_config:
        app.config.update(test_config)

    @app.route("/<pokemon>", methods=["GET"])
    def get_pokemon(pokemon):
        cache = get_cache()
        cached = cache.get(pokemon)
        if cached:
            return {
                "name": pokemon,
                "description": cached,
            }

        with handle_errors():
            description = get_pokemon_description(pokemon)
            translated = translate_to_shakespeare(description)

        cache.save(pokemon, translated)
        return {
            "name": pokemon,
            "description": translated,
        }

    return app


@contextmanager
def handle_errors():
    try:
        yield
    except InvalidPokemonError:
        abort(404)
    except TooManyRequestsError:
        abort(429)
    except UnknownAPIError:
        # Something wrong with the API call that we don't know how to fix.
        abort(500)
