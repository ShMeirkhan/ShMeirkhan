import re

def match_string(text):
    pattern = r'ab*'
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

s=input()
print(match_string(s))