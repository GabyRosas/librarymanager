
from models.GeneralModel import GeneralModel
import psycopg2


class UserModel(GeneralModel):
    def __init__(self):
        super().__init__()
        self.table = 'users'

    def create(self, data):
        return super().create(self.table, data)

    def read(self, criteria):
        return super().read(self.table, criteria)

    def update(self, data, criteria):
        return super().update(self.table, data, criteria)

    def delete(self, criteria):
        return super().delete(self.table, criteria)

    def is_duplicate(self, data):
        identification_number = data.get('identification_number')
        query = f"SELECT * FROM {self.table} WHERE identification_number = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (identification_number,))
                return cursor.fetchall()
        except psycopg2.Error as e:
            print(f"Error al buscar usuario en la base de datos: {e}")
            return None



