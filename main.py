
from src.controllers.CategoryController import CategoryController


def main():
    category_controller = CategoryController()
    print("     Creacion de categorias")
    data = {
        'category_name': 'Magic',
        'description': 'Magic books'
    }

    result = category_controller.create_category(data)
    print(result)

    """if result > 0:
        print('Categoría creada exitosamente.')
    else:
        print('La categoría no fue creada.')
"""

    print("     Actualizacion de categorias")

    data_update = {
        'category_name': 'Biography',
        'description': 'Books that detail the life story of me.'
    }
    criteria_update = {
        'category_name': 'Biography'
    }

    update_result = category_controller.update_category(data_update, criteria_update)
    print(update_result)


    print("     lectura de categorias")
    criteria_read = {
        'category_name': 'Mystery'
    }

    read_result = category_controller.read_category(criteria_read)
    print(read_result)


    print("     Borrado de categorias")
    criteria_delete = {
        'category_name': 'Magic'
    }

    delete_result = category_controller.delete_category(criteria_delete)
    print(delete_result)


""" # Obtener todos los usuarios
    category = user_controller.get_users()
    print(users)"""

if __name__ == "__main__":
    main()