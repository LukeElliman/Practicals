name = input("Enter your name: ")
MENU = """(H)ello
(G)oodbye
(Q)uit"""
print(MENU)
choice=input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello " + name)
        print()
    elif choice == "G":
        print("Goodbye " + name)
        print()
    else:
        print("Invalid choice")
        print()
    print(MENU)
    choice = input(">>> ").upper()
print("Thank You")