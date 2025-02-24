import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()
    return snake_str
s = input()
snake_str = camel_to_snake(s)
print(snake_str) 