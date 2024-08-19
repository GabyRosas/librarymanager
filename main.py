from src.controllers.BookController import BookController


def main():
    controller = BookController()

    update_data = {'title': 'CARLAAAAAA'}
    criteria = {'isbn': '978-3-16-148412-0'}
    print(controller.update_book(update_data, criteria))


if __name__ == "__main__":
    main()

