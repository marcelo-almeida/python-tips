# Use rpartition when you want to get the last information from a split
value = 'personal_email@domain.com'
print(value.rpartition('@')[2])
# rpartition will returns ('personal_email', '@', 'domain.com')
# result: domain.com

value = 'domain.com'
print(value.rpartition('@')[2])
# rpartition will returns ('', '', 'domain.com')
# result: domain.com

# build strings from a list
name = 'personal_email'
domain = 'domain.com'
print('@'.join([name, domain]))
# result: personal_email@domain.com
print(f'{name}@{domain}')
# result: personal_email@domain.com
