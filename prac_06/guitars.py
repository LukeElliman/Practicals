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

    if guitars:
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            # print("Guitar {}, {} ({}), worth ${} {}".format(i + 1,
            #                                                 guitar.name,
            #                                                 guitar.year,
            #                                                 guitar.cost,
            #                                                 vintage_string))
            print("Guitar {}, {guitar.name} ({guitar.year}), "
                  "worth ${guitar.cost} {}".format(i + 1, vintage_string,
                                                   guitar=guitar,))
    else:
        print("No guitars")

main()
