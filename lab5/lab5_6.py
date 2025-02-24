import re

def replace_characters(text):
    result = re.sub(r'[ ,.]', ':', text)
    return result
s=input()
output_text = replace_characters(s)
print(output_text)