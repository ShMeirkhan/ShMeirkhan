def write_list(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        f.write("\n".join(data))
filename=input()
write_list(filename, ["Apple", "Banana", "Cherry"])
def read_list(file):
    with open(file, 'r', encoding='utf-8') as f:
        print(f.read())

read_list(filename)