import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connection = None
cursor = None

try:
    connection = psycopg2.connect("host=localhost user=postgres password=postgres")
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);
    cursor = connection.cursor()
    cursor.execute('DROP DATABASE IF EXISTS test;')
    cursor.execute('CREATE DATABASE test;')
except Exception as exc:
    print(exc)
finally:
    if cursor:
        cursor.close()

    if connection:
        connection.close()


