LOWER = 33
UPPER = 127

MAX_COLUMNS = 10
MIN_COLUMNS = 2


def main():
    #Step 1
    character = str(input("Enter a letter: "))
    print("The ASCII code for {} is {}".format(character, ord(character)))

    number = get_number(LOWER, UPPER)
    print("The character for {} is {}".format(number, chr(number)))


def get_number(lower=LOWER, upper=UPPER):
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


main()