import re

def snake_to_camel(snake_str):
    return re.sub(r'_([a-z])', lambda match: match.group(1).upper(), snake_str)

snake_str = "this_is_a_snake_case_string"
camel_str = snake_to_camel(snake_str)
print(camel_str)