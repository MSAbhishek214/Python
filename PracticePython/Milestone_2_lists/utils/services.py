"""
This module has the services associated with a library and deals with the user interaction
"""
from utils import database


def add_book_service():
    """ 
    A method that takes in the user inputs needed for adding a book to the database.
    """
    book_name = input('Enter name of the book: ')
    book_author = input('Enter author of the book: ')

    database.add_book(book_name, book_author)

    print('Book added successfully')


def list_books_service():
    """ 
    A method that returns all books currently in a list.
    """
    for book in books:
        print('{} by {}'.format(book['name'], book['author']))


def mark_as_read_service():
    """ 
    A method that marks a book as read by settings its read variable boolean value to True, given a book name.
    """
    name = input('Enter name of the book you want to mark as read: ')

    for book in books:
        if book['name'] == name:
            book['read'] = True

    print(f'Book {name} marked as read.')


def delete_book_service():
    """
    A method that deletes a book by removing the book from the list, given book name.
    """
    global books

    name = input('Enter name of the book you wish to delete from library: ')

    books = [book for book in books if book['name'] != name]

    print(f'Book {name} removed from library.')