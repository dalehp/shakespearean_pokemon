import pytest

from shakespearean_pokemon.exceptions import UnknownAPIError
from shakespearean_pokemon.translate import translate_to_shakespeare


def test_get_translate_success(mock_translateapi):
    assert translate_to_shakespeare("test") == (
        "Charizard flies 'round the sky in search of powerful opponents. 't "
        "breathes fire of such most wondrous heat yond 't melts aught. However,  "
        "'t nev'r turns its fiery breath on any opponent weaker than itself."
    )


def test_get_translate_error(mock_translateapi_error):
    with pytest.raises(UnknownAPIError):
        translate_to_shakespeare("test")
