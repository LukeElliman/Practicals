"""Ask user for numbers, processes said numbers
Luke Elliman
"""

AMOUNT_OF_NUMBERS = 5
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    """Ask user for numbers, process and print numbers"""
    numbers = []
    for i in range(AMOUNT_OF_NUMBERS):
        valid_input = False
        while not valid_input:
            try:
                user_number = int(input("Number: "))
                numbers.append(user_number)
                valid_input = True
            except ValueError:
                print("Input must be an integer.")

    number_print(numbers)

    name_input = str(input("Enter your name: "))
    if username_check(usernames, name_input):
        print("Access granted")
    else:
        print("Access denied")

    #Practice 2 question
    numbers = []
    number_amount = 1
    valid_input = False
    while not valid_input:
        try:
            user_number = int(input("Number {}: ".format(number_amount)))
            if user_number >= 0:
                number_amount += 1
                numbers.append(user_number)
            else:
                valid_input = True
        except ValueError:
            print("Input must be an integer.")

    number_print(numbers)


def first_number(numbers: list) -> int:
    """Get first number from list"""
    value = numbers[0]
    return value


def last_number(numbers: list) -> int:
    """Get last number from list"""
    value = numbers[-1]
    return value


def min_number(numbers: list) -> int:
    """Get smallest number from list"""
    value = min(numbers)
    return value


def max_number(numbers: list) -> int:
    """Get largest number from list"""
    value = max(numbers)
    return value


def avg_number(numbers: list) -> float:
    """Get average number from list"""
    value = sum(numbers)/len(numbers)
    return value


def number_print(numbers):
    """Prints numbers after operations are applied"""
    print("The first number is {0}".format(first_number(numbers)))
    print("The last number is {0}".format(last_number(numbers)))
    print("The smallest number is {0}".format(min_number(numbers)))
    print("The largest number is {0}".format(max_number(numbers)))
    print("The average number is {0:,.2f}".format(avg_number(numbers)))


def username_check(names: list, user_input: str) -> bool:
    """Check if user input is in a list"""
    for name in range(len(names)):
        if user_input == names[name]:
            return True
    return False


main()
