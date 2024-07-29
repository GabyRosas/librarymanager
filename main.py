from src.controllers.UserController import UserController

def main():
    user_controller = UserController()

    # Crear un nuevo usuario
    new_user = {
        'name': 'John Doe',
        'identification_number': 'MEM129',
        'email': 'john@example.com',
        'phone': '555-7890',
        'address': '123 Elm St'
    }

    result = user_controller.create_user(new_user)
    print(result)  # Verifica el resultado de la operación de creación

    # Obtener todos los usuarios
    users = user_controller.get_users()
    print(users)

if __name__ == "__main__":
    main()


"""from src.controllers.UserController import UserController

user = UserController()
name = 'Seda'
password = 'holi589'

register = user.create_user(name, password)

print(register)

"""