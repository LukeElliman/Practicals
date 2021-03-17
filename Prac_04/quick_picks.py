"""
Generates a set of numbers into a list
Luke Elliman
"""

NUMBER_OF_LINES = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Prints row of numbers consisting of 6 columns"""
    rows = row_amount_get()


def row_amount_get():
    """Ask user for number of rows, validates input is correct"""
    valid_input = False
    while not valid_input:
        try:
            number_of_rows = int(input("How many rows "))
            if number_of_rows >= 1:
                valid_input = True
                return number_of_rows
            else:
                print("Number be above 0")
        except ValueError:
            print("Number must be an integer")


main()



