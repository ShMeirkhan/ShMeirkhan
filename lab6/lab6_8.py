import os
path = input()
if os.path.exists(path):
    print("Путь существует.")
    file_name = os.path.basename(path)
    print("Имя файла:", file_name)
    directory_part = os.path.dirname(path)
    print("Часть каталога:", directory_part)
else:
    print("Путь не существует.")