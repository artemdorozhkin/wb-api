class TokenIsMissing(Exception):
    pass


class InvalidToken(Exception):
    pass


class TokenIsMalformed(Exception):
    pass


class TokenNotFound(Exception):
    pass


class TokenIsNotApplicable(Exception):
    pass


class ToManyRequests(Exception):
    pass


class RequestError(Exception):
    pass
