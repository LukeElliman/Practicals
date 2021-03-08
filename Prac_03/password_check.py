def main():
    """Stores the main part of the program"""
    password = input("Enter the password: ")
    valid_password_length = False
    while not valid_password_length:
        try:
            password_length = int(input("Enter the password length: "))
            while password_length <= 0:
                print("Password length must be above 0")
                password_length = int(input("Enter the password length: "))
            else:
                valid_password_length = True
        except ValueError:
            print("Input must be an integer")
    while len(password) < password_length:
        print("Not long enough")
        password = input("Enter the password: ")

    for i in password:
        print(end="*")

main()

