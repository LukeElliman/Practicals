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

    print(numbers)


main()