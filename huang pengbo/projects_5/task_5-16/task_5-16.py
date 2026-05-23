import psycopg2

def main():
    connection = None
    cursor = None
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5435",
            user="postgres",
            password="student",
            database="student_task"
        )
        print("Подключение к базе данных прошло успешно!")

        cursor = connection.cursor()

        cursor.execute("SELECT id, name, category FROM products LIMIT 5;")
        rows = cursor.fetchall()

        print("\nРезультаты запроса (первые 5 товаров):")
        for row in rows:
            print(f"ID: {row[0]}, Название: {row[1]}, Категория: {row[2]}")

    except Exception as error:
        print(f"Ошибка при подключении или выполнении запроса: {error}")

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None:
            connection.close()
            print("\nСоединение закрыто.")

if __name__ == "__main__":
    main()