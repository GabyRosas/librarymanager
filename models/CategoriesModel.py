from models.GeneralModel import GeneralModel
import psycopg2


class CategoryModel(GeneralModel):
    def __init__(self):
        super().__init__()
        self.table = 'categories'

    def create(self, data):
        return super().create(self.table, data)

    def update(self, data, criteria):
        return super().update(self.table, data, criteria)

    def category_exists(self, data):
        category_name = data.get('category_name')
        query = f"SELECT COUNT(*) FROM {self.table} WHERE category_name = %s"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (category_name,))
                result = cursor.fetchone()
                return result[0] > 0
        except psycopg2.Error as e:
            print(f"Error al verificar la existencia de la categoría '{category_name}': {e}")
            return False