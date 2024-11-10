import psycopg2


def get_db_connection():
    conn = psycopg2.connect(
        dbname="inmobiliaria",
        user="postgres",
        password="LordC",
        host="localhost",
        port="5432",
    )
    return conn
