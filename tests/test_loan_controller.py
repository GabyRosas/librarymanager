import pytest
from datetime import date, timedelta
from src.controllers.LoanController import LoanController

@pytest.fixture
def loan_controller(mocker):
    loan_model_mock = mocker.Mock()
    return LoanController(loan_model_mock)

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
    assert result == {"loan_id": 1}

    mock_create.assert_called_once_with(loan_data)
    mock_update_inventory.assert_called_once_with(1, -1)

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

def test_notify_due_today(loan_controller, mocker):
    mocker.patch.object(loan_controller.loan_model, 'get_loans_due_today', return_value=[{
        'user_id': 1,
        'due_date': date.today().isoformat()
    }])
    mock_send_notification = mocker.patch.object(loan_controller, 'send_notification')
    mocker.patch.object(loan_controller.loan_model, 'get_user_email', return_value='user@example.com')

    loan_controller.notify_due_today()

    mock_send_notification.assert_called_once_with(
        'user@example.com',
        'Recordatorio de devolución',
        f'Tu préstamo vence hoy ({date.today().isoformat()}). Por favor, devuelve el libro a tiempo.'
    )

def test_notify_overdue(loan_controller, mocker):
    mocker.patch.object(loan_controller.loan_model, 'get_overdue_loans', return_value=[{
        'user_id': 1,
        'due_date': (date.today() - timedelta(days=1)).isoformat()
    }])
    mock_send_notification = mocker.patch.object(loan_controller, 'send_notification')
    mocker.patch.object(loan_controller.loan_model, 'get_user_email', return_value='user@example.com')

    loan_controller.notify_overdue()

    mock_send_notification.assert_called_once_with(
        'user@example.com',
        'Notificación de préstamo atrasado',
        f'Tu préstamo venció el {(date.today() - timedelta(days=1)).isoformat()} y aún no has devuelto el libro. Por favor, devuélvelo lo antes posible.'
    )

def test_notify_due_in_3_days(loan_controller, mocker):
    mocker.patch.object(loan_controller.loan_model, 'get_loans_due_in_3_days', return_value=[{
        'user_id': 1,
        'due_date': (date.today() + timedelta(days=3)).isoformat()
    }])
    mock_send_notification = mocker.patch.object(loan_controller, 'send_notification')
    mocker.patch.object(loan_controller.loan_model, 'get_user_email', return_value='user@example.com')

    loan_controller.notify_due_in_3_days()

    mock_send_notification.assert_called_once_with(
        'user@example.com',
        'Recordatorio de devolución próxima',
        f'Tu préstamo vence en 3 días ({(date.today() + timedelta(days=3)).isoformat()}). Por favor, asegúrate de devolver el libro a tiempo.'
    )

def test_return_book_success(loan_controller, mocker):
    mock_update_inventory = mocker.patch.object(loan_controller.loan_model, 'update_book_inventory')
    mock_update_loan_status = mocker.patch.object(loan_controller.loan_model, 'update_loan_status', return_value=True)

    result = loan_controller.return_book(1, 1)
    assert result == "Libro devuelto exitosamente."

    mock_update_inventory.assert_called_once_with(1, 1)
    mock_update_loan_status.assert_called_once_with(1, 'returned')
