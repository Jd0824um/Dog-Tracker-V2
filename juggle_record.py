from Simple_SQL_App import db
from Simple_SQL_App.holder import Holder
import logging


def main():
    db.setup()

    quit = 'q'
    choice = None

    while choice is not quit:
        choice = get_choice(display_menu())


# Displays a menu for the user to choose an option to do
def display_menu():
    print('''
        1. Show record holders
        2. Add record holder
        3. Delete record holder
        4. Update catches of a record holder
        5. Search for a record holder
        Q. Quit
    ''')

    choice = input("Enter your selection: \n")

    logging.info("Choice " + choice + " was selected")
    return choice


# Gets the choice and goes to the corresponding method
def get_choice(choice):
    if choice == '1':
        show_record_holders()
    elif choice == '2':
        add_record_holder()
    elif choice == '3':
        delete_record_holder()
    elif choice == '4':
        update_record_holder()
    elif choice == '5':
        search_record_holder()
    elif choice == 'q' or 'Q':
        return choice
    else:
        print("Enter a valid selection please")


def add_record_holder():
    name = input("Enter name: \n")
    country = input("Enter country: \n")
    count = input("Enter # of catches:\n")

    new_holder = db.add_holder(Holder(name, country, count))

    if new_holder == None:
        print('Record holder ' + str(name) + ' was not added.')
    else:
        print('Record holder ' + str(new_holder) + ' added!')


# Shows all record holders
def show_record_holders():
    holders = db.show_holders()

    if len(holders) == 0:
        print("No Records")

    for holder in holders:
        print(holder)


# Deletes a record holder by calling the database and deleting by name
def delete_record_holder():
    name = input("Enter name: \n")
    delete_holder = db.delete_holder(name)

    if delete_holder:
        print(name + 'was deleted!')
    else:
        print('Record was not deleted. Please double check the spelling of the name.')


# Updates a record holder
def update_record_holder():
    name = input("Enter name: \n")
    count = input("Enter # of catches:\n ")
    update_holder = db.update_catches(name, count)

    if update_holder:
        print ('Record holder ' + str(name) + ' was updated with ' + count + ' catches.')
    else:
        print('Record was not updated. Double check the spelling of the name of the record holder you wish to update')


# Searches for a record holder
def search_record_holder():
    name = input("Enter name: \n")
    search_holder = db.search_holder(name)
    print(search_holder)


main()
