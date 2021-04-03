"""
Practice question
names to address
"""

name_to_address = {"Robert Cop": "Dunworth Street", "Bob Timmy": "Sesame Street"}


def main():
    choice = menu()
    while choice != "Q":
        if choice == "A":
            name = str(input("Enter a name: ")).strip().title()
            address = str(input("Enter an address: ")).strip().title()
            name_to_address[name] = address
            choice = menu()
        if choice == "E":
            name = str(input("Enter a name for an address you want to change: ")).strip().title()
            if name in name_to_address:
                address = str(input("Enter an address: ")).strip().title()
                name_to_address[name] = address
            else:
                print("That name is not valid")
            choice = menu()
        if choice == "P":
            name = str(input("Enter a name for address you want printed: ")).strip().title()
            if name in name_to_address:
                print("{0} lives at {1}".format(name, name_to_address[name]))
            else:
                print("That name is not valid")
            choice = menu()


def menu():
    """Print menu text and gets user choice"""
    menu_choice_options = ("A", "E", "P", "Q")
    menu_options = """Menu:
A - Add a name and address
E - Edit an address
P - Print a name and address
Q - quit"""
    print(menu_options)
    choice = str(input(">>> ")).upper()
    while choice not in menu_choice_options:
        print("Invalid menu choice")
        print(menu_options)
        choice = str(input(">>> ")).upper()
    else:
        return choice



main()