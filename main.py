from src.controllers.BookController import BookController


def main():
    controller = BookController()

    update_data = {'title': 'CARLAAAAAA'}
    criteria = {'isbn': '978-3-16-148412-0'}
    print(controller.update_book(update_data, criteria))


if __name__ == "__main__":
    main()



"""from src.controllers.UserController import UserController

user = UserController()
name = 'Seda'
password = 'holi589'

register = user.create_user(name, password)

print(register)

"""