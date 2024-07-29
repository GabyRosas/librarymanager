from models.GeneralModel import GeneralModel
from models.InterfaceModel import InterfaceModel

class UserModel(GeneralModel, InterfaceModel):  # herencia múltiple
    def __init__(self):
        super().__init__()  # Llamada al constructor de la clase base
        self.table = 'users'  # Nombre de la tabla en la base de datos

    def create(self, data):
        return super().create(self.table, data)

    def validate_data(self, data):
        # Aquí puedes agregar la lógica para validar los datos del usuario.
        # Esto es solo un ejemplo básico.
        required_fields = ['name', 'membership_number', 'email', 'phone', 'address']
        for field in required_fields:
            if field not in data or not data[field]:
                return False
        return True

    def search(self, criteria=None):
        # Implementa la lógica de búsqueda si es necesario
        pass

    # Asegúrate de implementar también los otros métodos abstractos de InterfaceModel
    def read(self, criteria=None):
        return super().read(self.table, criteria)

    def update(self, data, criteria):
        return super().update(self.table, data, criteria)

    def delete(self, criteria):
        return super().delete(self.table, criteria)


"""from config.DbConnection import Connection


class UsersModel:

    def __init__(self):
        self.db = Connection()

    def create_user(self, username, password):
        query = "INSERT INTO users(name, password) VALUES(%s, %s)"
        params = (username, password)
        return self.db.update_query(query, params)

    # def get_user(id)
    # def edit_user(id)
    # def delete_user(id)
"""