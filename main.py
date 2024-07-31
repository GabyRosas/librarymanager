from src.controllers.LoanController import LoanController


def main():
   # Crear una instancia del controlador de préstamos
    loan_controller = LoanController()

    # Datos del préstamo a añadir
    loan_data = {
        'user-id': 1,
        'book_id': 1,
        'loan_date': '2024-08-31',
        'return_date' : '',
        'due_date': '2024-08-31'

    }

    # Añadir un nuevo préstamo
    result = loan_controller.create_loan(loan_data)
    print(f"Resultado al crear préstamo: {result}")




main()

"""from src.controllers.UserController import UserController

user = UserController()
name = 'Seda'
password = 'holi589'

register = user.create_user(name, password)

print(register)

"""