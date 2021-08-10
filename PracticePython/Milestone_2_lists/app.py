'''
Our main application interface code goes here
'''
# import the services module that in itself communicates with the database module
from utils import services
MENU_PROMPT = """
Book store actions are given below. Choose one of them to perform specific action!

- 'a' to add a book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit the store

Enter your choice: """

# a dictionary of user options with related actions
user_options = {
    'a': database.add_book,
    'l': database.list_books,
    'r': database.mark_as_read,
    'd': database.delete_book
}

# menu for our application
def menu():
    user_input = input(MENU_PROMPT)
    while user_input != 'q':
        if user_input in user_options:
            execute_method = user_options[user_input]
            execute_method()
        else:
            print('Unknown command! Please try again with a valid command.')

        user_input = input(MENU_PROMPT)


# Run the menu indefinetly until user selects q
menu()