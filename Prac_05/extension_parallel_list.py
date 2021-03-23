"""Convert parallel list to dictionary"""

names = ["Jack", "Jill", "Harry"]
dates_of_birth = [(12, 4, 1999), (1, 1, 2000), (27, 3, 1982)]
name_to_birthday = {}

for date, name in enumerate(names):
    name_to_birthday[name] = dates_of_birth[date]

for i in range(5):
    name = str(input("Enter a name "))
    birthday = str(input("Enter a birthday (in form dd/mm/yyyy) "))
    birthday_split = birthday.split("/")
    birthday_tuple = tuple(int(number) for number in birthday_split)
    name_to_birthday[name] = birthday_tuple


print(name_to_birthday)
