x_value = int(input("Enter the x value: "))
y_value = int(input("Enter the y value: "))

MENU = """Input (1) for even numbers from x to y
Input (2) for odd numbers from x to y
Input (3) for squared numbers from x to y
Input (4) to exit the program"""
print(MENU)
choice = str(input(">>> "))
while choice != "4":
    if choice == "1":
        for i in range(x_value, int((y_value)/2) + 1, 1):
            print(i * 2, end=' ')
        print()
    if choice == "2":
        for i in range(x_value, int((y_value)/2), 1):
            print(i * 2 + 1, end=' ')
        print()
    if choice == "3":
        for i in range(x_value, int(y_value), 1):
            print(i ** 2, end=' ')
        print()
    print(MENU)
    choice = str(input(">>> "))
print("Bye")
