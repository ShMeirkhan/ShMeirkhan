
import re

def split_by_uppercase(s):
    return re.findall(r'[A-Z][^A-Z]*', s)
s=input()
print(split_by_uppercase(s))
