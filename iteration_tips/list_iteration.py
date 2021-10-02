# Iterating list to fill other list with values
web_list = ['categories', 'products', 'profile', 'services']
print([item for item in web_list])
# result: ['categories', 'products', 'profile', 'services']

print([item for item in web_list if item != 'profile'])
# result: ['categories', 'products', 'services']

print([item for item in web_list if item in ['profile', 'services', 'configuration']])
# result: ['profile', 'services']

print([{'type': item} for item in web_list])
# result: [{'type': 'categories'}, {'type': 'products'}, {'type': 'profile'}, {'type': 'services'}]
