import re

def match_pattern(text):
    pattern = r'.*ab$'
    if re.match(pattern, text):
        return True
    else:
        return False

s=input()
print(match_pattern(s))
