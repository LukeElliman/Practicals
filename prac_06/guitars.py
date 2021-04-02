from prac_06.guitar import Guitar


def main():
    guitars = []

    print("My guitars!")

    name = str(input("Name: "))
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print("{} added".format(guitar_to_add))
        name = str(input("Name: "))

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

main()
