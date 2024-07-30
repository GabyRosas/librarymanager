
from src.controllers.CategoryController import CategoryController


def main():
    category_controller = CategoryController()

    data = {
        'category_name': 'Astrology',
        'description': 'Astrology books'
    }

    result = category_controller.create_category(data)
    print(result)  # Verifica el resultado de la operación de creación

    """if result > 0:
        print('Categoría creada exitosamente.')
    else:
        print('La categoría no fue creada.')
"""

#Actualizacion de categorias

    data_update = {
        'category_name': 'Magic',
        'description': 'Magic description'
    }
    criteria_update = {
        'category_name': 'Magic Updated'
    }

    update_result = category_controller.update_category(data_update, criteria_update)
    print(update_result)  # Verifica el resultado de la operación de actualización


""" # Obtener todos los usuarios
    category = user_controller.get_users()
    print(users)"""

if __name__ == "__main__":
    main()