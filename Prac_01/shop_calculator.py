number_of_items = int(input("How many items do you have: "))

while number_of_items >= 0:
    total = 0
    for i in range(0, int(number_of_items)):
        price_of_item = float(input("Price of item: "))
        total = float(total) + float(price_of_item)
    if total > 100:
        total = 0.9 * total
        print("Total price for " + str(number_of_items) + " items is " + "{:.2f}".format(total))
        print()
    else:
        print("Total price for " + str(number_of_items) + " items is " + "{:.2f}".format(total))
        print()
    number_of_items = int(input("How many items do you have: "))
while number_of_items < 0:
    print("Invalid number of items!")
    print()
    number_of_items = int(input("How many items do you have: "))
