# Iterating list to fill other list with values
web_list = ['categories', 'products', 'profile', 'services']
print([item for item in web_list])
# ['categories', 'products', 'profile', 'services']
print([item for item in web_list if item != 'profile'])
# ['categories', 'products', 'services']
print([{'type': item} for item in web_list])
# [{'type': 'categories'}, {'type': 'products'}, {'type': 'profile'}, {'type': 'services'}]
