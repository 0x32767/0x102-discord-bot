from errors.base_error import BaseError


class IllegalCharacterError(BaseError):
    msg = "Illegal character {}"
