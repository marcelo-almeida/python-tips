# You can use a dict to simulate a multiple if/else statements.
def calculator_with_if_else(key: str, x: float, y: float):
    if key == 'sum':
        return x + y
    elif key == 'sub':
        return x - y
    elif key == 'mul':
        return x * y
    elif key == 'div':
        return x / y
    else:
        return None


def calculator_with_dict(key: str, x: float, y: float):
    return {
        'sum': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(key, lambda: None)()


# Validating empty data
def validate_list_not_empty(field: list):
    return True if field else False


def validate_string_not_empty(field: str):
    return True if field else False
