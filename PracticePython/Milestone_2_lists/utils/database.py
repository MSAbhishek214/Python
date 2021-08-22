"""
This python file is to store data into and retrieve from files (which are basically permanent storage solutions)
Data Structure used: Files
Author: Abhishek Rotti
"""
# Define an empty list for the books
import abc
from os import name

books = []


def _save_to_file(books):
    with open('PracticePython/Milestone_2_lists/MyLibrary.csv', 'w+') as file:
        for book in books:
            file.write('{},{},{}\n'.format(
                book['name'], book['author'], book['read']))


def add_book(book_name, book_author):
    """ 
    A method to add a book to a list, given its name.
    """
    with open('PracticePython/Milestone_2_lists/MyLibrary.csv', 'a') as file:
        file.write(f'{book_name},{book_author},false\n')


def list_books():
    """ 
    A method that returns all books currently in a list.
    """
    with open('PracticePython/Milestone_2_lists/MyLibrary.csv', 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    temp_books = []
    for line in lines:
        temp_books.append({
            'name': line[0],
            'author': line[1],
            'read': line[2]
        })

    return temp_books


def mark_as_read(name):
    """ 
    A method that marks a book as read by settings its read variable boolean value to True, given a book name.
    """
    books = list_books()

    for book in books:
        if book['name'] == name:
            book['read'] = 'true'

    _save_to_file(books)


def delete_book(name):
    """
    A method that deletes a book by removing the book from the list, given book name.
    """
    books = list_books()

    new_book = [book for book in books if book['name'] != name]

    _save_to_file(new_book)
