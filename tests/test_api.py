import json

import pytest

from shakespearean_pokemon import create_app
from shakespearean_pokemon.cache import get_cache


@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture(autouse=True)
def clear_cache():
    c = get_cache()
    c._cache.clear()


def test_get_pokemon(client, mock_pokeapi, mock_translateapi):
    data = client.get("/charizard").get_json()
    assert data == {
        "name": "charizard",
        "description": (
            (
                "Charizard flies 'round the sky in search of powerful opponents. 't "
                "breathes fire of such most wondrous heat yond 't melts aught. "
                "However,  't nev'r turns its fiery breath on any opponent weaker than "
                "itself."
            )
        ),
    }


def test_get_invalid_pokemon(client, mock_pokeapi):
    r = client.get("/chorizard")
    assert r.status_code == 404


def test_get_unknown_error(client, mock_pokeapi):
    r = client.get("/test_error")
    assert r.status_code == 500


def test_cached_call(client, mock_pokeapi, mock_translateapi):
    client.get("/charizard").get_json()
    client.get("/charizard").get_json()

    assert mock_pokeapi.call_count == 1
    assert mock_translateapi.call_count == 1
