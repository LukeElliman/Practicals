def main():
    """Stores the main part of the program"""
    password = input("Enter the password: ")
    password_length = int(input("Enter the password length: "))
    password_length = password_length_verifier(password_length)
    while len(password) < password_length:
        print("Not long enough")
        password = input("Enter the password: ")

    for i in password:
        print(end="*")


def password_length_verifier(length):
    """See if the inputted password_length is an integer"""
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


main()

