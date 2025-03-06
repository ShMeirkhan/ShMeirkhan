def delete_file(filename):
    try:
        f = open(filename, 'r')
        f.close()
        open(filename, 'w').close()
        print("File deleted")
    except FileNotFoundError:
        print("No file")
filename=input()
delete_file(filename)