import psycopg2

# PostgreSQL серверіне қосылу
conn = psycopg2.connect(
    dbname="lab10",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 1. Шаблонмен іздеу (name немесе phone бойынша)
def search_phonebook(pattern):
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", ('%' + pattern + '%', '%' + pattern + '%'))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Жазбалар табылмады.")

# 2. Қолданушыны қосу немесе телефон нөмірін жаңарту
def insert_or_update_user(name, phone):
    cur.execute("SELECT 1 FROM phonebook WHERE name = %s", (name,))
    if cur.fetchone():  # Егер қолданушы бар болса
        cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (phone, name))
        print(f"{name} қолданушысының телефоны жаңартылды.")
    else:  # Қолданушы жоқ болса
        cur.execute("INSERT INTO phonebook(name, phone) VALUES (%s, %s)", (name, phone))
        print(f"{name} қосылды.")
    
    # Жаңартылған кестені көру
    view_updated_table()
# 3. Көп қолданушыны қосу (bulk insert)
def bulk_insert_users(names, phones):
    for name, phone in zip(names, phones):
        if phone.isdigit() and len(phone) in range(10, 16):  # Телефон нөмірінің дұрыстығын тексеру
            cur.execute("INSERT INTO phonebook(name, phone) VALUES (%s, %s)", (name, phone))
        else:
            print(f"Қате телефон: {phone} ({name})")
    conn.commit()
    print("Барлық деректер қосылды.")
    
    # Жаңартылған кестені көру
    view_updated_table()

# 4. Пагинациямен деректерді алу (limit, offset)
def get_phonebook_page(limit, offset):
    cur.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Қосымша жазбалар жоқ.")

# 5. Аты немесе телефоны бойынша деректерді өшіру
def delete_by_name_or_phone(value):
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (value, value))
    conn.commit()
    print(f"{value} бойынша барлық деректер өшірілді.")
    
    # Жаңартылған кестені көру
    view_updated_table()

# 6. Жаңартылған кестені көрсету
def view_updated_table():
    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()
    print("\nЖаңартылған телефон кітапшасы:")
    for row in rows:
        print(row)

while True:
    print("\n===== PHONEBOOK МӘЗІРІ =====")
    print("1. Шаблон бойынша іздеу")
    print("2. Қолданушы қосу немесе жаңарту")
    print("3. Көп қолданушыны қосу")
    print("4. Пагинациямен деректерді алу")
    print("5. Деректерді өшіру")
    print("6. Жаңартылған кесте")
    print("0. Шығу")

    choice = input("Таңда: ")
    if choice == "1":
        pattern = input("Шаблонды енгізіңіз: ")
        search_phonebook(pattern)
    elif choice == "2":
        name = input("Қолданушының атын енгізіңіз: ")
        phone = input("Телефон номерін енгізіңіз: ")
        insert_or_update_user(name, phone)
    elif choice == "3":
        names = input("Атауларды (арқылы үтірмен бөлінген) енгізіңіз: ").split(",")
        phones = input("Телефондарды (арқылы үтірмен бөлінген) енгізіңіз: ").split(",")
        bulk_insert_users(names, phones)
    elif choice == "4":
        limit = int(input("Көрсетілетін жазбалар саны (limit): "))
        offset = int(input("Жазбалардан басталатын орын (offset): "))
        get_phonebook_page(limit, offset)
    elif choice == "5":
        value = input("Қандай аты немесе телефонды өшіргіңіз келеді? ")
        delete_by_name_or_phone(value)
    elif choice == "6":
        view_updated_table()
    elif choice == "0":
        break
    else:
        print("Қате таңдау!")

cur.close()
conn.close()