"""
Ascii table
Luke Elliman
"""
LOWER = 33
UPPER = 127

MAX_COLUMNS = 10
MIN_COLUMNS = 2


def main():
    """Runs the main program"""
    character = str(input("Enter a letter: "))
    print("The ASCII code for {} is {}".format(character, ord(character)))

    number = get_number(LOWER, UPPER)
    print("The character for {} is {}".format(number, chr(number)))

    columns = get_column(MIN_COLUMNS, MAX_COLUMNS)
    number_of_values = UPPER - LOWER + 1
    rows = number_of_values // columns


def get_number(lower, upper):
    """Gets input from user about value they want in a certain range"""
    valid_input = False
    while not valid_input:
        try:
            value = int(input("Enter a number ({0}-{1}) ".format(lower, upper)))
            if value < lower or value > upper:
                print("The value must be between {0} and {1}".format(lower, upper))
            else:
                valid_input = True
        except ValueError:
            print("You must input an integer")
    return value


def get_column(lower, upper):
    """Gets input from user on how many columns they want"""
    valid_input = False
    while not valid_input:
        try:
            value = int(input("Enter a number of columns ({0}-{1}) ".format(lower, upper)))
            if value < lower or value > upper:
                print("The value must be between {0} and {1}".format(lower, upper))
            else:
                valid_input = True
        except ValueError:
            print("You must input an integer")
    return value


main()