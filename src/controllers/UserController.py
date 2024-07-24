from models.UsersModel import UsersModel


class UserController:

    def __init__(self):
        self.user_model = UsersModel()

    def create_user(self, username, password):
        self.user_model.create_user(username, password)
        return dict(status_code=200,
                    response='El usuario se hacreado de manera exitosa',
                    result=[username, password])

    # def verify_user()
    # def get_user(id)
    # def edit_user(id)
    # def delete_user(id)


