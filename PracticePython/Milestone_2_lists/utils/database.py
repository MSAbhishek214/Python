"""
This python file is to store data into and retrieve from lists (which are basically in memory database objects, almost)
Data Structure used: Lists
Author: Abhishek Rotti
"""
# Define an empty list for the books
books = []


def add_book():
    """ 
    A method to add a book to a list, given its name.
    """
    book_name = input('Enter name of the book: ')
    book_author = input('Enter author of the book: ')

    books.append(
        {
            'name': book_name,
            'author': book_author,
            'read': False
        }
    )
    print(f'Book {book_name} added to your library.')


def list_books():
    """ 
    A method that returns all books currently in a list.
    """
    for book in books:
        print('{} by {}'.format(book['name'], book['author']))


def mark_as_read():
    """ 
    A method that marks a book as read by settings its read variable boolean value to True, given a book name.
    """
    name = input('Enter name of the book you want to mark as read: ')

    for book in books:
        if book['name'] == name:
            book['read'] = True

    print(f'Book {name} marked as read.')

def delete_book():
    """
    A method that deletes a book by removing the book from the list, given book name.
    """
    global books

    name = input('Enter name of the book you wish to delete from library: ')

    books = [book for book in books if book['name'] != name]

    print(f'Book {name} removed from library.')
