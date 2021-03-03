LOWER = 33
UPPER = 127

MAX_COLUMNS = 10
MIN_COLUMNS = 2

#Step 1
letter_to_number = str(input("Enter a letter: "))
print("The ASCII code for {} is {}".format(letter_to_number, ord(letter_to_number)))

number_to_letter = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))

while number_to_letter < LOWER or number_to_letter > UPPER:
    number_to_letter = int(input("Enter a number between {} and {}: ".format(LOWER, UPPER)))

print("The character for {} is {}".format(number_to_letter, chr(number_to_letter)))

#Step 2
for i in range(LOWER, UPPER + 1):
    print("{:3} {:>4}".format(i, chr(i)))

#Step 3
columns = int(input("Enter the number of columns: "))
while columns < MIN_COLUMNS or columns > MAX_COLUMNS:
    print("Please enter a value between {} and {}".format(MIN_COLUMNS, MAX_COLUMNS))
    columns = int(input("Enter the number of columns: "))
number_of_values = UPPER - LOWER + 1
rows = number_of_values // columns

#Version 1 a lot easier to understand
value = LOWER
for row in range(rows):
    for column in range(columns):
        print("{:6} {:>2}".format(value, chr(value)), end="")
        value += 1
    print()

starting_value = value
for value in range(starting_value, UPPER + 1):
    print("{:6} {:>2}".format(value, chr(value)), end="")
print("\n")

#Version 2
for row in range(rows + 1):
    starting_value = LOWER + row
    value = starting_value
    for column in range(columns - 1):
        value_to_print = value + (column * rows)
        print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
        value += 1

    value_to_print = value + ((column + 1) * rows)
    if value_to_print <= UPPER:
        print("{:6} {:>2}".format(value_to_print, chr(value_to_print)), end="")
    print()
