"""
This python file is to store data into and retrieve from lists (which are basically in memory database objects, almost)
Data Structure used: Lists
Author: Abhishek Rotti
"""
# Define an empty list for the books
books = []


def add_book(book_name, book_author):
    """ 
    A method to add a book to a list, given its name.
    """
    books.append(
        {
            'name': book_name,
            'author': book_author,
            'read': False
        }
    )
    return books[-1]


def list_books():
    """ 
    A method that returns all books currently in a list.
    """
    return books


def mark_as_read(name):
    """ 
    A method that marks a book as read by settings its read variable boolean value to True, given a book name.
    """

    for book in books:
        if book['name'] == name:
            book['read'] = True


def delete_book(name):
    """
    A method that deletes a book by removing the book from the list, given book name.
    """
    global books

    books = [book for book in books if book['name'] != name]

