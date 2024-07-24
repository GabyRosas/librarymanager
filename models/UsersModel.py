from config.DbConnection import Connection


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
