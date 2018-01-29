from Simple_SQL_App import db

def main():
    db.setup()

    quit = 'q'
    choice = None

    while choice is not quit:
        choice = display_menu()
        get_choice(choice)

# Displays a menu for the user to choose an option to do
def display_menu():
    print('''
        1. Show record holders
        2. Add record holder
        3. Delete record holder
        4. Update catches of a record holder
        Q. Quit
    ''')

    choice = input("Enter your selection: \n")

    # Validation input
    while choice > 4 or choice < 1:
        choice = int(input("Enter your selection between 1 and 4 or Q to quit: \n"))

    return choice

def get_choice():
    if choice == 1:
        show_record_holders():
    elif choice == 2:
        add_record_holder():
    elif choice == 3:
        delete_record_holder():
    else choice == 4:
        quit():
    else:
        print("Enter a valid selection please")
