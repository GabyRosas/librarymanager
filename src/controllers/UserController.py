from models.UsersModel import UserModel


class UserController:
    def __init__(self):
        self.model = UserModel()

    def create_user(self, data):
        if self.model.is_duplicate(data):
            identification_number = data.get('identification_number')
            return {"message": f"Usuario con DNI/NIE '{identification_number}' ya se encuentra registrado"}, 409
        result = self.model.create(data)
        if result is not None:
            return {"message": f"Usuario registrado", "rowcount": result}, 201
        return {"message": "Error al crear usuario"}, 500

    def read_user(self, name=None, identification_number=None, phone=None):
        criteria = {}
        if name:
            criteria['name'] = name
        if identification_number:
            criteria['identification_number'] = identification_number
        if phone:
            criteria['phone'] = phone
        return self.model.read(criteria)

    def update_user(self, user_id, new_data):
        criteria = {'user_id': user_id}
        return self.model.update(new_data, criteria)

    def delete_user(self, user_id):
        criteria = {'user_id': user_id}
        return self.model.delete(criteria)


