"""
Generates a set of numbers into a list
Luke Elliman
"""

import random

NUMBERS_PER_LINES = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Prints row of numbers consisting of 6 columns"""
    rows = row_amount_get()
    list_generator(rows)


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


def list_generator(rows: int):
    """Generate and print 6 number per row, check if there are duplicates, sorts"""
    for row in range(rows):
        numbers = []
        for number in range(NUMBERS_PER_LINES):
            quick_pick = random.randint(MINIMUM, MAXIMUM)
            while quick_pick in numbers:
                quick_pick = random.randint(MINIMUM, MAXIMUM)
            numbers.append(quick_pick)
        numbers.sort()
        print(numbers)



main()



