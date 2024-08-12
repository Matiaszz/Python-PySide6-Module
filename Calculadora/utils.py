CHARS = '0123456789.'


def isValidNumber(str: str) -> bool:
    valid = False
    try:
        float(str)
        valid = True
    except ValueError:
        valid = False

    return valid
