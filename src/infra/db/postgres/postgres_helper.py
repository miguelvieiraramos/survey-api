import os.path

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from src import settings


class PostgresHelper:
    URI = {
        'host': 'localhost',
        'database': 'postgres',
        'user': 'postgres',
        'password': 'postgres'
    }

    @staticmethod
    def get_connection(host: str, database: str, user: str, password: str):
        return psycopg2.connect(host=host, database=database, user=user, password=password)

    @staticmethod
    def one(query: str, parameters: tuple):
        connection = None
        cursor = None
        try:
            connection = PostgresHelper.get_connection(**PostgresHelper.URI)
            cursor = connection.cursor()
            cursor.execute(query, parameters)
            connection.commit()
            return cursor.fetchall()
        finally:
            if cursor:
                cursor.close()

            if connection:
                connection.close()

    @staticmethod
    def init_db():
        connection = None
        cursor = None
        try:
            connection = psycopg2.connect(host='localhost', user='postgres', password='postgres')
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            cursor.execute('DROP DATABASE IF EXISTS test;')
            cursor.execute('CREATE DATABASE test;')

            connection = psycopg2.connect(**PostgresHelper.URI)
            cursor = connection.cursor()
            with open(os.path.join(settings.BASE_DIR, 'db.sql'), 'r') as file:
                sql = file.read()
            cursor.execute(sql)
            connection.commit()

        except Exception as exc:
            print(exc)

        finally:
            if cursor:
                cursor.close()

            if connection:
                connection.close()

    @staticmethod
    def close_db():
        connection = None
        cursor = None
        try:
            connection = psycopg2.connect(host='localhost', user='postgres', password='postgres')
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            cursor.execute('DROP DATABASE IF EXISTS test;')

        except Exception as exc:
            print(exc)

        finally:
            if cursor:
                cursor.close()

            if connection:
                connection.close()
