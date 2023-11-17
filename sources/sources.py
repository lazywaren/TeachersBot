import os


def get_available_books() -> list:
    ignore_list = ['__init__.py', __file__.split('/')[-1],'__pycache__']
    available_books = []
    for book_name in os.listdir('sources'):
        if book_name not in ignore_list:
            available_books.append(book_name)
    return available_books