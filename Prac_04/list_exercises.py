"""Ask user for numbers, processes said numbers
Luke Elliman
"""

AMOUNT_OF_NUMBERS = 5


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

    print("The first number is {0}".format(first_number(numbers)))
    print("The last number is {0}".format(last_number(numbers)))
    print("The smallest number is {0}".format(min_number(numbers)))

    print(numbers)


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

main()
