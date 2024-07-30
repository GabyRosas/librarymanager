from models.CategoriesModel import CategoryModel

class CategoryController:
    def __init__(self):
        self.category_model = CategoryModel()

    def create_category(self, data):
        if self.category_model.category_exists(data):
            category_name = data.get('category_name')
            print(f"La categoría '{category_name}' ya existe.")
            return 0
        result = self.category_model.create(data)
        return result

    def update_category(self, data, criteria):
        if not self.category_model.category_exists(criteria):
            category_name = criteria.get('category_name')
            print(f"La categoría '{category_name}' no existe.")
            return 0
        result = self.category_model.update(data, criteria)
        if result > 0:
            return {'Categoría actualizada exitosamente.'}
        else:
            return {'La categoría no fue actualizada.'}
        #return result