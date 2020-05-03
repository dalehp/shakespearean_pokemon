class InvalidPokemonError(Exception):
    pass


class UnknownAPIError(Exception):
    """Unexpected errors from external API. Should probably handle this better for
    certain scenarios, e.g. retry on 503?"""

    pass


class TooManyRequestsError(Exception):
    pass
