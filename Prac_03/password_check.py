def main():
    """Stores the main part of the program"""
    password = input("Enter the password: ")
    password_length = int(input("Enter the password length: "))
    password_length = password_length_verifier(password_length)
    password = user_password_check(password, password_length)
    for i in password:
        print(end="*")


def password_length_verifier(length):
    """See if the inputted password length is an integer"""
    valid_length = False
    while not valid_length:
        try:
            while length <= 0:
                print("Password length must be above 0")
                length = int(input("Enter the password length: "))
            else:
                valid_length = True
        except ValueError:
            print("Input must be an integer")
    return length


def user_password_check(password,length):
    """Checks if the inputted password is less than the password length"""
    while len(password) < length:
        print("Not long enough")
        password = input("Enter the password: ")
    return password


main()

