# Use rpartition when you want to get the last information from a split
value = 'personal_email@domain.com'
print(value.rpartition('@')[2])
# rpartition will returns ('personal_email', '@', 'domain.com')

value = 'domain.com'
print(value.rpartition('@')[2])
# rpartition will returns ('', '', 'domain.com')

# build strings from a list
print('@'.join(['personal_email', 'domain.com']))
# personal_email@domain.com
