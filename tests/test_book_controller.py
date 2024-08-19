from unittest.mock import MagicMock
from src.controllers.BookController import BookController


"""
Este archivo contiene pruebas para el controlador de libros utilizando pytest.
Las pruebas cubren los siguientes escenarios:
Creación exitosa de un libro.
Creación de un libro cuando el libro no esté aun en la base de datos.
Fallo en la creación de un nuevo libro.
Creación exitosa de un libro.
Fallo al crear un libro.
Fallo al actualizar el inventario al crear un libro.

Las pruebas utilizan una implementación de prueba para simular la lógica del modelo de creación de libros en la base de datos y comprobar los resultados esperados.
"""


def test_create_book_success():
    """
       Escenario: Test para crear un libro exitosamente.

       Given: Un libro que no está duplicado.

       When: Se intenta crear el libro.

       Then: El libro se crea con éxito.
             El mensaje indica que el libro se ha creado correctamente.
    """
    mock_model = MagicMock()
    mock_model.is_duplicate.return_value = False
    mock_model.create.return_value = 1

    controller = BookController()
    controller.model = mock_model

    book_data = {
        'title': 'Prueba',
        'author': 'Prueba',
        'isbn': '1234567890'
    }

    result, status_code = controller.create_book(book_data)

    assert status_code == 201
    assert result == {"message": "Libro creado exitosamente", "rowcount": 1}


def test_create_book_duplicate():
    """
        Escenario: Test para controlar que un libro esté o no duplicado.

        Given: Un libro que ya existe en el sistema.

        When: Se intenta crear el libro.

        Then: Se rechaza la creación del libro.
              El mensaje indica que el libro ya existe en el inventario.
     """
    mock_model = MagicMock()
    mock_model.is_duplicate.return_value = True

    controller = BookController()
    controller.model = mock_model

    book_data = {
        'title': 'Duplicado',
        'author': 'Duplicado',
        'isbn': '9876543210'
    }

    result, status_code = controller.create_book(book_data)

    assert status_code == 409
    assert "ya existe en el inventario" in result["message"]


def test_get_books_success():
    """
        Escenario: Test para obtener la lista de libros.

        Given: Una lista de libros disponibles en el sistema.

        When: Se solicitan los libros.

        Then: Se devuelve la lista de libros.
              Los títulos de los libros son correctos.
    """
    mock_model = MagicMock()
    mock_model.read.return_value = [{'title': 'Libro 1'}, {'title': 'Libro 2'}]

    controller = BookController()
    controller.model = mock_model

    result, status_code = controller.get_books()

    assert status_code == 200
    assert len(result) == 2
    assert result[0]['title'] == 'Libro 1'
    assert result[1]['title'] == 'Libro 2'


def test_update_book_success():
    """
        Escenario: Test para actualizar un libro.

        Given: Datos de libro actualizados y criterios de selección válidos.

        When: Se intenta actualizar el libro con nuevos datos.

        Then: El libro se actualiza.
              Se envía un mensaje conforme el libro fue actualizado exitosamente.
    """
    mock_model = MagicMock()
    mock_model.update.return_value = 1

    controller = BookController()
    controller.model = mock_model

    book_data = {'title': 'Actualización Título'}
    criteria = {'isbn': '1234567890'}

    result, status_code = controller.update_book(book_data, criteria)

    assert status_code == 200
    assert result == {"message": "Libro actualizado exitosamente", "rowcount": 1}



