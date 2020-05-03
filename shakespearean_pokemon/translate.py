import requests
from requests.exceptions import ConnectionError

from .exceptions import TooManyRequestsError, UnknownAPIError


class TranslateAPIError(Exception):
    pass


def translate_to_shakespeare(text: str) -> str:
    try:
        r = requests.post(
            "https://api.funtranslations.com/translate/shakespeare.json",
            data={"text": text},
        )
    except ConnectionError:
        raise UnknownAPIError()

    if r.status_code == 429:
        raise TooManyRequestsError()
    if r.status_code != 200:
        print(r.status_code)
        raise UnknownAPIError()

    data = r.json()
    return data["contents"]["translated"]
