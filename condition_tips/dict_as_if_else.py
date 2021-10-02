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


print(calculator_with_if_else(key='sum', x=1, y=1))  # result: 2
print(calculator_with_dict(key='sum', x=1, y=1))  # result: 2
