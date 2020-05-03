import requests
from requests.exceptions import ConnectionError


class TranslateAPIError(Exception):
    pass


def translate_to_shakespeare(text: str) -> str:
    try:
        r = requests.post(
            "https://api.funtranslations.com/translate/shakespeare.json",
            data={"text": text},
        )
    except ConnectionError:
        raise TranslateAPIError()

    if r.status_code != 200:
        raise TranslateAPIError()

    data = r.json()
    return data["contents"]["translated"]
