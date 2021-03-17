"""
Code for indefinite strings program
Luke Elliman
"""


def main():
    strings = string_get()
    print(strings)


def string_get():
    strings = []
    blank_string = False
    while not blank_string:
        user_input = str(input("Enter a string: "))
        if user_input == "":
            blank_string = True
        else:
            strings.append(user_input)
    return strings


main()