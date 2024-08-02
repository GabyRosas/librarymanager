from models.GeneralModel import GeneralModel
import psycopg2

class LoanModel(GeneralModel):
    def __init__(self):
        super().__init__()
        self.table = 'loans'

    def create(self, data):
        return super().create(self.table, data)

    def read(self, criteria=None):
        return super().read(self.table, criteria)

    def update(self, data, criteria):
        return super().update(self.table, data, criteria)

    def delete(self, criteria):
        return super().delete(self.table, criteria)

    def is_book_available(self, book_id):
        query = "SELECT * FROM books WHERE copies_available = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (book_id,))
                result = cursor.fetchone()
                if result:
                    return result[0] > 0
                return False
        except psycopg2.Error as e:
            print(f"Error al verificar la disponibilidad del libro: {e}")
            return False

    def update_book_inventory(self, book_id, increment=True):
        query = "UPDATE books SET copies_available = copies_available + 1 WHERE book_id = %s" if increment else "UPDATE books SET copies_available = copies_available - 1 WHERE book_id = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (book_id,))
                self.connection.commit()
                return True
        except psycopg2.Error as e:
            print(f"Error al actualizar el inventario del libro: {e}")
            self.connection.rollback()
            return False

    def get_book_id_from_loan(self, loan_id):
        query = "SELECT book_id FROM loans WHERE loan_id = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (loan_id,))
                result = cursor.fetchone()
                if result:
                    return result[0]
                else:
                    return None
        except psycopg2.Error as e:
            print(f"Error al obtener el ID del libro: {e}")
            return None


    def get_loans_due_today(self):
        query = "SELECT * FROM loans WHERE due_date = CURRENT_DATE"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error al obtener los préstamos con vencimiento hoy: {e}")
            return []

    def get_overdue_loans(self):
        query = "SELECT * FROM loans WHERE due_date < CURRENT_DATE AND return_date IS NULL"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error al obtener los préstamos atrasados: {e}")
            return []

    def get_loans_due_in_3_days(self):
        query = "SELECT * FROM loans WHERE due_date = CURRENT_DATE + INTERVAL '3 days' AND return_date IS NULL"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error al obtener los préstamos con vencimiento en 3 días: {e}")
            return []

