import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="postgres",  # попробуй это
        host="localhost",
        port="5432"
    )
    print("Успешное подключение!")
except Exception as e:
    print("Ошибка подключения:", e)
