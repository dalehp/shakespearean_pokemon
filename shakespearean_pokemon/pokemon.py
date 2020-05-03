from typing import Optional, List

import requests
from requests.exceptions import ConnectionError


class InvalidPokemonError(Exception):
    pass


class PokemonAPIError(Exception):
    """Unexpected errors from pokeapi. Should probably handle this better for certain
    scenarios, e.g. retry on 503?"""

    pass


def get_pokemon_description(name: str) -> str:
    try:
        r = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{name}")
    except ConnectionError:
        raise PokemonAPIError()

    if r.status_code == 404:
        raise InvalidPokemonError(f"{name} is not a valid pokemon name.")
    elif r.status_code != 200:
        raise PokemonAPIError

    data = r.json()

    return _extract_description(data["flavor_text_entries"])


def _extract_description(flavor_texts: List[dict]) -> str:
    """Get the first english flavour text from a provided list."""
    for flavor_text in flavor_texts:
        if flavor_text["language"]["name"] == "en":
            return flavor_text["flavor_text"]
    raise PokemonAPIError("No english flavour text found.")
