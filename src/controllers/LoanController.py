from models.LoansModel  import LoanModel

class LoanController:
    def __init__(self):
        self.loan_model = LoanModel()

    def create_loan(self, loan_data):
        book_id = loan_data.get('book_id')
        if not book_id or not self.loan_model.is_book_available(book_id):
            return "El libro no está disponible o no existe."

        loan_data['status'] = 'borrowed'
        result = self.loan_model.create(loan_data)
        return result
    def return_book(self, loan_id, user_email):
        criteria = {'id': loan_id}
        loan_data = {'status': 'returned'}  # Asume que hay un campo 'status' en la tabla de préstamos
        result = self.loan_model.update_loan(loan_data, criteria)
        if result:
            self.send_notification(user_email, "Libro devuelto", "Tu libro ha sido devuelto exitosamente.")
        return result

    def notify_users(self):
        loans = self.loan_model.read_loans({'status': 'borrowed'})
        for loan in loans:
            user_email = loan.get('user_email')
            due_date = loan.get('due_date')
            self.send_notification(user_email, "Recordatorio de devolución", f"Recuerda devolver tu libro antes del {due_date}")

    def send_notification(self, to_email, subject, body):
        print(f"Enviar correo a: {to_email}")
        print(f"Asunto: {subject}")
        print(f"Cuerpo: {body}")

    def get_loans(self, criteria=None):
        return self.loan_model.read_loans(criteria)
