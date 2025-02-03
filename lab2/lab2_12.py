my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print(my_dict['name'])

my_dict['email'] = 'alice@example.com'
print(my_dict)

my_dict['age'] = 26
print(my_dict)

del my_dict['city']
print(my_dict)

email = my_dict.pop('email')
print(email)
print(my_dict)

my_dict.clear()
print(my_dict)

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

last_item = my_dict.popitem()
print(last_item)
print(my_dict)

my_dict.update({'country': 'USA'})
print(my_dict)

age = my_dict.get('age', 'Not found')
print(age)

nested_dict = {
    'person1': {'name': 'Alice', 'age': 25},
    'person2': {'name': 'Bob', 'age': 30}
}
print(nested_dict)

copied_dict = my_dict.copy()
print(copied_dict)

for key, value in my_dict.items():
    print(f'{key}: {value}')

keys = list(my_dict.keys())
i = 0
while i < len(keys):
    key = keys[i]
    print(f'{key}: {my_dict[key]}')
    i += 1