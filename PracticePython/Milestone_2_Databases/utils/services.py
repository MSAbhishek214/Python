"""
This module has the services associated with a library and deals with the user interaction
"""
from PracticePython.Milestone_2_Databases.utils import database


def create_book_table_service():
    """
    A method that takes no arguments but calls the database table creation method
    """
    database.create_book_table()


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
    library = database.get_all_books()
    
    if len(library) == 0:
        print("Your library looks empty. Go ahead and add a few books to it!")
    else:
        for book in library:
            print('{} by {}'.format(book['name'], book['author']))


def mark_as_read_service():
    """ 
    A method that marks a book as read by settings its read variable boolean value to True, given a book name.
    """
    name = input('Enter name of the book you want to mark as read: ')

    database.mark_as_read(name)

    print(f'Book {name} marked as read.')


def delete_book_service():
    """
    A method that deletes a book by removing the book from the list, given book name.
    """
    name = input('Enter name of the book you wish to delete from library: ')

    database.delete_book(name)

    print(f'Book {name} removed from library.')
