import re

def find_sequences(text):
    pattern = r'[A-Z][a-z]+'
    matches = re.findall(pattern, text)
    return matches

text = input()
sequences = find_sequences(text)
print(sequences)