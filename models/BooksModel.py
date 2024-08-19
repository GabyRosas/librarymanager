from models.GeneralModel import GeneralModel
import psycopg2


class BooksModel(GeneralModel):
    def __init__(self):
        super().__init__()

    def create(self, data):
        return super().create('books', data)

    def read(self, criteria=None):
        return super().read('books', criteria)

    def update(self, data, criteria):
        return super().update('books', data, criteria)

    def delete(self, criteria):
        return super().delete('books', criteria)

    def is_duplicate(self, isbn):
        query = "SELECT * FROM books WHERE isbn = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (isbn,))
                return cursor.fetchone() is not None
        except psycopg2.Error as e:
            print(f"Error al verificar duplicados en la tabla books: {e}")
            return False

