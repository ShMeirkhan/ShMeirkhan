import re

def match_pattern(text):
    pattern = r'.*ab{2,3}'
    if re.match(pattern, text):
        return True
    else:
        return False
s=input()
print(match_pattern(s))