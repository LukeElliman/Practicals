password = input("Enter the password: ")
password_length = int(input("Enter the password length: "))
while len(password) < password_length:
    print("Not long enough")
    password = input("Enter the password: ")

for i in password:
    print(end = "*")