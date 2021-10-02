# Validating empty data
def validate_list_not_empty(field: list):
    return True if field else False


def validate_string_not_empty(field: str):
    return True if field else False


print(validate_list_not_empty(field=[]))  # result: False
print(validate_list_not_empty(field=['value']))  # result: True
print(validate_list_not_empty(field=[{'key': 'value'}]))  # result: True
print(validate_string_not_empty(field='')) # result: False
