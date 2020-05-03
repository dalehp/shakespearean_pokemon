import json

import pytest

from shakespearean_pokemon import create_app


@pytest.fixture
def app():
    app = create_app({"TESTING": True})
    yield app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


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
