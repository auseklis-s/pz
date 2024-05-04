import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('car_rental.db')
cur = conn.cursor()

# Создание таблицы, если она не существует
cur.execute('''CREATE TABLE IF NOT EXISTS Clients (
                id INTEGER PRIMARY KEY,
                full_name TEXT,
                car_brand TEXT,
                rental_period TEXT,
                amount REAL,
                prepayment TEXT
            )''')
conn.commit()

while True:
    print("1. Добавить клиента")
    print("2. Показать список клиентов")
    print("3. Выйти")
    choice = input("Выберите действие: ")

    if choice == '1':
        full_name = input("Введите ФИО клиента: ")
        car_brand = input("Введите марку авто: ")
        rental_period = input("Введите срок проката: ")
        amount = float(input("Введите сумму: "))
        prepayment = input("Есть ли предоплата (да/нет): ")

        cur.execute("INSERT INTO Clients (full_name, car_brand, rental_period, amount, prepayment) VALUES (?, ?, ?, ?, ?)",
                    (full_name, car_brand, rental_period, amount, prepayment))
        conn.commit()
        print("Клиент добавлен!")

    elif choice == '2':
        cur.execute("SELECT * FROM Clients")
        clients = cur.fetchall()
        for client in clients:
            print(f"{client[0]} : {client[1]} - {client[2]} - {client[3]} - {client[4]} - {client[5]}")

    elif choice == '3':
        conn.close()
        break

    else:
        print("Некорректный выбор. Попробуйте снова.")