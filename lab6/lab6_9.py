def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())
filename=input()
print("Количество строк:", count_lines(filename))