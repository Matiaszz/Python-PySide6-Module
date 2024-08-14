import re
NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str) -> bool:
    return bool(NUM_OR_DOT_REGEX.search(string))


def convertToNumber(str: str) -> int | float:
    number = float(str)
    if number.is_integer():
        number = int(number)

    return number


def isValidNumber(string: str) -> bool:
    valid = False
    try:
        float(string)
        valid = True
    except ValueError:
        valid = False

    return valid


def isEmpty(text: str):
    return len(text) == 0
