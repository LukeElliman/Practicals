import random
import string

# password length and character type choices
password_length = int(input("How long do you want your password: "))
while password_length < 4:
    print("Enter a password length above 4: ")
    password_length = int(input("How long do you want your password: "))

upper_choice = str(input("Do you want uppercase characters. Y or N: ")).upper()
while upper_choice != "Y" and upper_choice != "N":
    print("Invalid choice")
    upper_choice = str(input("Do you want uppercase characters. Y or N: ")).upper()

if upper_choice == "Y":
    upper_choice = True
else:
    upper_choice = False

lower_choice = str(input("Do you want lowercase characters. Y or N: ")).upper()
while lower_choice != "Y" and lower_choice != "N":
    print("Invalid choice")

if lower_choice == "Y":
    lower_choice = True
else:
    lower_choice = False

numeric_choice = str(input("Do you want numeric characters. Y or N: ")).upper()
while numeric_choice != "Y" and numeric_choice != "N":
    print("Invalid choice")

if numeric_choice == "Y":
    numeric_choice = True
else:
    numeric_choice = False

special_choice = str(input("Do you want special case characters. Y or N: ")).upper()
while special_choice != "Y" and special_choice != "N":
    print("Invalid choice")

if special_choice == "Y":
    special_choice = True
else:
    special_choice = False

# Setup to decide on what characters to use.
# Variables named x_required are used to determine if the password has the required characters for that type
if upper_choice == True:
    UPPER_LIST = string.ascii_uppercase
    upper_required = 1
else:
    UPPER_LIST = ""
    upper_required = 0
    print("There are no uppercase characters")

if lower_choice == True:
    LOWER_LIST = string.ascii_lowercase
    lower_required = 1
else:
    LOWER_LIST = ""
    lower_required = 0
    print("There are no lowercase characters")

if numeric_choice == True:
    NUMERIC_LIST = string.digits
    numeric_required = 1
else:
    NUMERIC_LIST = ""
    numeric_required = 0
    print("There are no numeric characters")

if special_choice == True:
    SPECIAL_LIST = string.punctuation
    special_required = 1
else:
    SPECIAL_LIST = ""
    special_required = 0
    print("There are no special characters")

ALL_LIST = (LOWER_LIST + UPPER_LIST + NUMERIC_LIST + SPECIAL_LIST)

# Password generation
# Boolean to set up a while loop to check if the password has required characters
required_password_characters = False
while required_password_characters == False:
    password = "".join(random.choice(ALL_LIST) for i in range(password_length))
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
        elif char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
        elif char in SPECIAL_LIST:
            count_special += 1
    if count_lower >= lower_required and count_upper >= upper_required and count_digit >= numeric_required and \
            count_special >= special_required:
        print("The password has the required characters")
        required_password_characters = True
    else:
        print("The password does not have required characters")

print("The password is {}".format(password))