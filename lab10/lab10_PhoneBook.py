import psycopg2
import csv

conn = psycopg2.connect(
    dbname="lab10",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        phone VARCHAR(20)
    );
""")
conn.commit()

# CSV-тен жүктеу
def load_from_csv():
    with open('psycopg2.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if len(row) >= 2:
                cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("CSV жүктелді!")

def insert_manually():
    name = input("Атың: ")
    phone = input("Нөмірің: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    conn.commit()
    print("Дерек қосылды!")

def update_entry():
    name = input("Қай атты өзгертеміз? ")
    new_phone = input("Жаңа номер: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    conn.commit()
    print("Жаңартылды!")

def query_data():
    filter_name = input("Аты бойынша іздеу: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", ('%' + filter_name + '%',))
    results = cur.fetchall()
    for row in results:
        print(row)

def delete_entry():
    name = input("Кімді өшіресіз (аты): ")
    cur.execute("DELETE FROM phonebook WHERE name = %s", (name,))
    conn.commit()
    print("Өшірілді!")

while True:
    print("\n===== PHONEBOOK МӘЗІРІ =====")
    print("1. CSV-тен жүктеу")
    print("2. Қолмен енгізу")
    print("3. Жаңарту")
    print("4. Іздеу")
    print("5. Өшіру")
    print("0. Шығу")

    choice = input("Таңда: ")
    if choice == "1":
        load_from_csv()
    elif choice == "2":
        insert_manually()
    elif choice == "3":
        update_entry()
    elif choice == "4":
        query_data()
    elif choice == "5":
        delete_entry()
    elif choice == "0":
        break
    else:
        print("Қате таңдау!")

cur.close()
conn.close()
