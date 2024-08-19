from models.LoansModel import LoanModel
from datetime import date

class LoanController:
    def __init__(self):
        self.loan_model = LoanModel()

    def create_loan(self, loan_data):
        book_id = loan_data.get('book_id')
        if not book_id or not self.loan_model.is_book_available(book_id):
            return "El libro no está disponible o no existe."

        result = self.loan_model.create(loan_data)
        if result:
            self.loan_model.update_book_inventory(book_id, increment=False)
        return "Préstamo creado con éxito." if result else "Error al crear el préstamo."

    def return_book(self, loan_id):
        book_id = self.loan_model.get_book_id_from_loan(loan_id)
        if not book_id:
            return "No se encontró el préstamo para el ID proporcionado."

        loan_update_result = self.loan_model.update({'return_date': date.today()}, {'loan_id': loan_id})
        if loan_update_result:
            inventory_update_result = self.loan_model.update_book_inventory(book_id, increment=True)
            if inventory_update_result:
                return "El libro ha sido devuelto y el inventario actualizado."
            else:
                return "Hubo un error al actualizar el inventario del libro."
        else:
            return "Hubo un error al actualizar la fecha de devolución del préstamo."

    def get_loans(self, criteria=None):
        return self.loan_model.read(criteria)

    def send_notification(self, to_email, subject, body):
        print(f"Enviar correo a: {to_email}")
        print(f"Asunto: {subject}")
        print(f"Cuerpo: {body}")

    def notify_due_today(self):
        loans_due_today = self.loan_model.get_loans_due_today()
        for loan in loans_due_today:
            user_email = loan.get('user_email')
            due_date = loan.get('due_date')
            self.send_notification(
                user_email,
                "Recordatorio de devolución",
                f"Tu préstamo vence hoy ({due_date}). Por favor, devuelve el libro a tiempo."
            )

    def notify_overdue(self):
        overdue_loans = self.loan_model.get_overdue_loans()
        for loan in overdue_loans:
            user_email = loan.get('user_email')
            due_date = loan.get('due_date')
            self.send_notification(
                user_email,
                "Notificación de préstamo atrasado",
                f"Tu préstamo venció el {due_date} y aún no has devuelto el libro. Por favor, devuélvelo lo antes posible."
            )

    def notify_due_in_3_days(self):
        loans_due_in_3_days = self.loan_model.get_loans_due_in_3_days()
        for loan in loans_due_in_3_days:
            user_email = loan.get('user_email')
            due_date = loan.get('due_date')
            self.send_notification(
                user_email,
                "Recordatorio de devolución próxima",
                f"Tu préstamo vence en 3 días ({due_date}). Por favor, asegúrate de devolver el libro a tiempo."
            )
