import pytest

from shakespearean_pokemon.pokemon import (
    _extract_description,
    PokemonAPIError,
    get_pokemon_description,
)


@pytest.fixture
def flav_text_entry():
    def _flav_text_entry(language, text):
        return {
            "flavor_text": text,
            "language": {
                "name": language,
                "url": "https://pokeapi.co/api/v2/language/9/",
            },
            "version": {
                "name": "alpha-sapphire",
                "url": "https://pokeapi.co/api/v2/version/26/",
            },
        }

    return _flav_text_entry


def test_get_pokemon_description_success(mock_pokeapi, mocker):
    patch = mocker.patch("shakespearean_pokemon.pokemon._extract_description")
    assert get_pokemon_description("charizard") == patch.return_value


def test_extract_description_single_valid(flav_text_entry):
    texts = [flav_text_entry(language="en", text="test")]
    assert _extract_description(texts) == "test"


def test_extract_description_single_invalid(flav_text_entry):
    texts = [flav_text_entry(language="jpn", text="test")]
    with pytest.raises(PokemonAPIError):
        _extract_description(texts)


def test_extract_description_multiple(flav_text_entry):
    texts = [
        flav_text_entry(language="jpn", text="test_1"),
        flav_text_entry(language="en", text="test_2"),
        flav_text_entry(language="en", text="test_3"),
    ]
    assert _extract_description(texts) == "test_2"
