import string

for letter in string.ascii_uppercase:
    open(f"{letter}.txt", "w").write(f"{letter}.txt file")