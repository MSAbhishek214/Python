"""
This python file is to store data into and retrieve from a database
Data Structure used: Sqlite3 Database
Author: Abhishek Rotti
"""
from typing import List, Dict

from .database_connection import DatabaseConnection


def create_book_table() -> None:
    """ 
    A method to create a library database and have a Books table in it.
    """
    with DatabaseConnection('library.db') as connection:
        cursor = connection.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS Books (name text primary key, author text, read integer)')


def add_book(book_name: str, book_author: str) -> None:
    """
    A method to add a book to Books table given the book name and author.
    """
    with DatabaseConnection('library.db') as connection:
        cursor = connection.cursor()

        cursor.execute('INSERT INTO Books VALUES(?, ?, 0)', (book_name, book_author))


def get_all_books() -> List[Dict]:
    """ 
    A method that returns all books currently in Books table.
    """
    with DatabaseConnection('library.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM Books')

        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    return books


def mark_as_read(book_name: str) -> None:
    """ 
    A method that marks a book as read by settings its read variable boolean value to True, given a book name.
    """
    with DatabaseConnection('library.db') as connection:
        cursor = connection.cursor()

        cursor.execute('UPDATE Books SET read=1 WHERE name=?', (book_name,))


def delete_book(book_name: str) -> None:
    """
    A method that deletes a book by removing the book from the list, given book name.
    """
    with DatabaseConnection('library.db') as connection:
        cursor = connection.cursor()

        cursor.execute('DELETE FROM Books WHERE name=?', (book_name,))
