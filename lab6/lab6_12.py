def copy_and_show(src, dst):
    try:
        with open(src, 'r', encoding='utf-8') as f1:
            data = f1.read()
    except FileNotFoundError:
        print("NO file")
        return

    with open(dst, 'w', encoding='utf-8') as f2:
        f2.write(data)

    with open(dst, 'r', encoding='utf-8') as f3:
        print(f3.read())


first = input()
second = input()
copy_and_show(first, second)
