import pytest


@pytest.fixture
def mock_pokeapi(requests_mock):
    with open("tests/pokeapi.json") as f:
        data = f.read()

    m1 = requests_mock.get(
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
    yield m1


@pytest.fixture
def mock_translateapi(requests_mock):
    with open("tests/translate.json") as f:
        data = f.read()

    return requests_mock.post(
        "https://api.funtranslations.com/translate/shakespeare.json", text=data,
    )


@pytest.fixture
def mock_translateapi_error(requests_mock):
    with open("tests/translate.json") as f:
        data = f.read()

    requests_mock.post(
        "https://api.funtranslations.com/translate/shakespeare.json",
        text="error",
        status_code=503,
    )
