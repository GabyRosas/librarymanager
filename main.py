from src.controllers.UserController import UserController

user = UserController()
name = 'Seda'
password = 'holi589'

register = user.create_user(name, password)

print(register)

