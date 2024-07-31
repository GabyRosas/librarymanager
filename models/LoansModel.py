from models.GeneralModel import GeneralModel

class LoanModel(GeneralModel):
    def __init__(self):
        super().__init__()

    def create_loan(self, loan_data):
        return self.create(loan_data)

    def update_loan(self, loan_data, criteria):
        return self.update(loan_data, criteria)

    def read_loans(self, criteria=None):
        return self.read(criteria)

    def delete_loan(self, criteria):
        return self.delete(criteria)

    def is_book_available(self, book_id):
        query = "SELECT status FROM books WHERE id = ?"  # aqui esta el error
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(query, (book_id,))
            result = cursor.fetchone()
            if result:
                return result[0] == 'available'
            return False
    def return_book(self, loan_id):
        #  las devoluciones de libros en la base de datos
        pass

    def notify_users(self):
        #  los usuarios que deben ser notificados
        pass

    def send_notification(self, to_email, subject, body):
        #  envían notificaciones a los usuarios
        pass
