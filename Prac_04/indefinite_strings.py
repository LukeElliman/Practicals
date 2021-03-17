"""
Code for indefinite strings program
Luke Elliman
"""


def main():
    strings = string_get()
    while len(strings) <= 0:
        print("You must enter at least one string")
        strings = string_get()
    print(repeated_string_check(strings))


def string_get():
    """Ask user for strings, until input is blank"""
    strings = []
    blank_string = False
    while not blank_string:
        user_input = str(input("Enter a string: "))
        if user_input == "":
            blank_string = True
        else:
            strings.append(user_input)
    return strings


def repeated_string_check(strings):
    """Check user input for repeated strings, makes list of repeated strings"""
    repeated_strings = []
    count = 1
    for string in strings:
        if string in repeated_strings:
            count += 1
        else:
            if string in strings[count:len(strings) + 1]:
                repeated_strings.append(string)
            count += 1
    return repeated_strings


main()