from config.DbConnection import Connection # para conection
from .InterfaceModel import InterfaceModel
import psycopg2  # para manejar errores de BBDD

class GeneralModel(InterfaceModel):
    def __init__(self):
        self.connection = Connection().get_connection()  # conection
#crud
    def create(self, table, data):
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, list(data.values()))
                self.connection.commit()
                return cursor.rowcount
        except psycopg2.Error as e:
            self.connection.rollback()
            print(f"Error al crear en la tabla {table}: {e}")

    def read(self, table, criteria=None):
        query = f"SELECT * FROM {table}"
        params = []
        if criteria:
            query += " WHERE " + ' AND '.join([f"{key}=%s" for key in criteria.keys()])
            params = list(criteria.values())
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, params)
                return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error al leer de la tabla {table}: {e}")
            return None

    def update(self, table, data, criteria):
        set_clause = ', '.join([f"{key}=%s" for key in data.keys()])
        where_clause = ' AND '.join([f"{key}=%s" for key in criteria.keys()])
        query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, list(data.values()) + list(criteria.values()))
                self.connection.commit()
                return cursor.rowcount
        except psycopg2.Error as e:
            self.connection.rollback()
            print(f"Error al actualizar en la tabla {table}: {e}")

    def delete(self, table, criteria):
        where_clause = ' AND '.join([f"{key}=%s" for key in criteria.keys()])
        query = f"DELETE FROM {table} WHERE {where_clause}"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, list(criteria.values()))
                self.connection.commit()
                return cursor.rowcount
        except psycopg2.Error as e:
            self.connection.rollback()
            print(f"Error al eliminar de la tabla {table}: {e}")

