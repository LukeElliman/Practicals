"""
Practice question
names to address
"""

name_to_address = {"Robert Cop": "Dunworth Street", "Bob Timmy": "Sesame Street"}


def main():
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