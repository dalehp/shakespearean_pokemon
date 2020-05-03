import pytest


@pytest.fixture
def mock_pokeapi(requests_mock):
    with open("tests/pokeapi.json") as f:
        data = f.read()

    requests_mock.get(
        "https://pokeapi.co/api/v2/pokemon-species/charizard", text=data,
    )
    requests_mock.get(
        "https://pokeapi.co/api/v2/pokemon-species/chorizard",
        text="error",
        status_code=404,
    )
    requests_mock.get(
        "https://pokeapi.co/api/v2/pokemon-species/test_error",
        text="error",
        status_code=504,
    )
