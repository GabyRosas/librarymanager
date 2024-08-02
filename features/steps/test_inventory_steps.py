import pytest
from pytest_bdd import scenario, given, when, then
from unittest.mock import MagicMock
from src.controllers.BookController import BookController


@scenario('../books.feature', 'Agregar libro')
def test_agregar_libro():
    pass


@pytest.fixture
def mock_books_model():
    return MagicMock()


@pytest.fixture
def book_controller(mock_books_model):
    return BookController(model=mock_books_model)


@given('la base de datos está lista')
def step_given_database_ready(mock_books_model):
    mock_books_model.is_duplicate.return_value = False
    mock_books_model.create.return_value = 1


@when('añado un libro')
def step_when_add_book(book_controller):
    book_data = {
        'title': 'La Casa de Bernarda ALba',
        'author': 'Carlos Ruiz Zafón',
        'isbn': '9788408043641'
    }
    result, status_code = book_controller.create_book(book_data)
    assert status_code == 201
    assert result == {"message": "Libro creado exitosamente", "rowcount": 1}


@then('el libro se añade correctamente')
def step_then_book_added():
    pass

