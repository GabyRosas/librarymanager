from models.UsersModel import UserModel
from src.controllers.UserController import UserController


def main():
    user_controller = UserController()

    new_user = {
        'name': 'Laura Duque',
        'identification_number': 'Z1315226X',
        'email': 'lau@example.com',
        'phone': '555-7890',
        'address': '456 Elm St'
    }

    result = user_controller.create_user(new_user)
    print(result)

    name = "name"
    identification_number = "identification_number"
    phone = "phone_number"

    users = user_controller.read_user(name=name, identification_number=identification_number, phone=phone)
    if users:
        for user in users:
            print(user)
    else:
        print("No se encontraron usuarios que coincidan con los criterios de búsqueda.")

    user_id = 1
    new_data = {
        'name': 'Juan Perez Updated',
        'phone': '555-4321'
    }
    updated_rows = user_controller.update_user(user_id, new_data)
    if updated_rows:
        print(f"Se actualizaron {updated_rows} filas.")
    else:
        print("No se pudo actualizar el usuario.")

    user_id_to_delete = 2
    deleted_rows = user_controller.delete_user(user_id_to_delete)
    if deleted_rows:
        print(f"Se eliminaron {deleted_rows} filas.")
    else:
        print("No se pudo eliminar el usuario.")


if __name__ == '__main__':
    main()
