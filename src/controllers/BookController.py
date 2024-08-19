from models.BooksModel import BooksModel


class BookController:
    def __init__(self):
        self.model = BooksModel()

    def create_book(self, data):
        isbn = data.get('isbn')
        if self.model.is_duplicate(isbn):
            return {"message": f"El libro con ISBN '{isbn}' ya existe en el inventario."}, 409
        result = self.model.create(data)
        if result is not None:
            return {"message": "Libro creado exitosamente", "rowcount": result}, 201
        return {"message": "Error al crear el libro"}, 500

    def get_books(self, criteria=None):
        result = self.model.read(criteria)
        if result is not None:
            return result, 200
        return {"message": "Error al consultar los libros"}, 500

    def update_book(self, data, criteria):
        result = self.model.update(data, criteria)
        if result is not None:
            return {"message": "Libro actualizado exitosamente", "rowcount": result}, 200
        return {"message": "Error al actualizar el libro"}, 500

    def delete_book(self, criteria):
        result = self.model.delete(criteria)
        if result is not None:
            return {"message": "Libro eliminado exitosamente", "rowcount": result}, 200
        return {"message": "Error al eliminar el libro"}, 500

