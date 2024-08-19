import pytest
from datetime import date, timedelta
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.controllers.LoanController import LoanController

"""
Este archivo contiene pruebas para el controlador de préstamos utilizando pytest.
Las pruebas cubren los siguientes escenarios:
Creación exitosa de un préstamo.
Creación de un préstamo cuando el libro no está disponible.
Fallo en la creación de un préstamo.
Devolución exitosa de un libro.
Fallo al devolver un libro cuando no se encuentra el préstamo.
Fallo al actualizar el inventario al devolver un libro.

Las pruebas utilizan una implementación de prueba para simular la lógica del modelo de préstamos y comprobar los resultados esperados
"""

@pytest.fixture
def loan_controller(mocker):
    controller = LoanController()
    controller.loan_model = mocker.Mock()
    return controller


"""
Escenario: Crear un préstamo exitosamente
Given: El libro con ID 1 está disponible
When: El usuario con ID 1 solicita un préstamo para el libro con ID 1
el préstamo se crea con la fecha de hoy y fecha de vencimiento en 7 días
Then: El préstamo debe ser creado exitosamente
el inventario del libro debe ser actualizado
"""
def test_create_loan_success(loan_controller, mocker):
    mocker.patch.object(loan_controller.loan_model, 'is_book_available', return_value=True)
    mock_create = mocker.patch.object(loan_controller.loan_model, 'create', return_value={"loan_id": 1})
    mock_update_inventory = mocker.patch.object(loan_controller.loan_model, 'update_book_inventory')

    loan_data = {
        'book_id': 1,
        'user_id': 1,
        'loan_date': date.today().isoformat(),
        'due_date': (date.today() + timedelta(days=7)).isoformat()
    }

    result = loan_controller.create_loan(loan_data)
    assert result == "Préstamo creado con éxito."

    mock_create.assert_called_once_with(loan_data)
    mock_update_inventory.assert_called_once_with(1, increment=False)

"""
Escenario: Intentar crear un préstamo cuando el libro no está disponible
Given: El libro con ID 1 no está disponible
When: El usuario con ID 1 solicita un préstamo para el libro con ID 1
Then: Se debe mostrar un mensaje de que el libro no está disponible
"""

def test_create_loan_book_not_available(loan_controller, mocker):
    mocker.patch.object(loan_controller.loan_model, 'is_book_available', return_value=False)
    mock_create = mocker.patch.object(loan_controller.loan_model, 'create')

    loan_data = {
        'book_id': 1,
        'user_id': 1,
        'loan_date': date.today().isoformat(),
        'due_date': (date.today() + timedelta(days=7)).isoformat()
    }

    result = loan_controller.create_loan(loan_data)
    assert result == "El libro no está disponible o no existe."
    assert mock_create.call_count == 0


"""
Escenario: Notificar los préstamos vencidos hoy
Given: Hay préstamos cuyo vencimiento es hoy
When: El sistema notifica a los usuarios sobre los préstamos vencidos hoy
Then: Los usuarios deben recibir un correo electrónico de recordatorio de devolución
"""
def test_notify_due_today(loan_controller, mocker):
    mocker.patch.object(loan_controller.loan_model, 'get_loans_due_today', return_value=[{
        'user_email': 'user@example.com',
        'due_date': date.today().isoformat()
    }])
    mock_send_notification = mocker.patch.object(loan_controller, 'send_notification')

    loan_controller.notify_due_today()

    mock_send_notification.assert_called_once_with(
        'user@example.com',
        'Recordatorio de devolución',
        f'Tu préstamo vence hoy ({date.today().isoformat()}). Por favor, devuelve el libro a tiempo.'
    )

"""
Escenario: Notificar préstamos atrasados
Given: Hay préstamos que vencieron ayer
When: El sistema notifica a los usuarios sobre los préstamos atrasados
Then: Los usuarios deben recibir un correo electrónico sobre el préstamo atrasado
"""

def test_notify_overdue(loan_controller, mocker):
    mocker.patch.object(loan_controller.loan_model, 'get_overdue_loans', return_value=[{
        'user_email': 'user@example.com',
        'due_date': (date.today() - timedelta(days=1)).isoformat()
    }])
    mock_send_notification = mocker.patch.object(loan_controller, 'send_notification')

    loan_controller.notify_overdue()

    mock_send_notification.assert_called_once_with(
        'user@example.com',
        'Notificación de préstamo atrasado',
        f'Tu préstamo venció el {(date.today() - timedelta(days=1)).isoformat()} y aún no has devuelto el libro. Por favor, devuélvelo lo antes posible.'
    )

"""
Escenario: Notificar préstamos que vencen en 3 días
Given: Hay préstamos que vencen en 3 días
When: El sistema notifica a los usuarios sobre los préstamos que vencen en 3 días
Then: Los usuarios deben recibir un correo electrónico de recordatorio sobre la próxima fecha de vencimiento
"""

def test_notify_due_in_3_days(loan_controller, mocker):
    mocker.patch.object(loan_controller.loan_model, 'get_loans_due_in_3_days', return_value=[{
        'user_email': 'user@example.com',
        'due_date': (date.today() + timedelta(days=3)).isoformat()
    }])
    mock_send_notification = mocker.patch.object(loan_controller, 'send_notification')

    loan_controller.notify_due_in_3_days()

    mock_send_notification.assert_called_once_with(
        'user@example.com',
        'Recordatorio de devolución próxima',
        f'Tu préstamo vence en 3 días ({(date.today() + timedelta(days=3)).isoformat()}). Por favor, asegúrate de devolver el libro a tiempo.'
    )

"""
Escenario: Devolver un libro exitosamente
Given: El libro con ID 1 está prestado al usuario con ID 1
When: El usuario devuelve el libro con ID 1
Then: El libro debe ser marcado como devuelto
el inventario del libro debe ser actualizado
"""

def test_return_book_success(loan_controller, mocker):
    mock_update_inventory = mocker.patch.object(loan_controller.loan_model, 'update_book_inventory')
    mock_update_loan_status = mocker.patch.object(loan_controller.loan_model, 'update', return_value=True)

    loan_controller.loan_model.get_book_id_from_loan.return_value = 1

    result = loan_controller.return_book(1)
    assert result == "El libro ha sido devuelto y el inventario actualizado."

    mock_update_inventory.assert_called_once_with(1, increment=True)
    mock_update_loan_status.assert_called_once_with({'return_date': date.today()}, {'loan_id': 1})

