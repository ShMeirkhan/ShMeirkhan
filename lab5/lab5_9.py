
import re

def insert_spaces(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

s=input()
output_text = insert_spaces(s)
print(output_text)
