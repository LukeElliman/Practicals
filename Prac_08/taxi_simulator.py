"""Program that simulates a taxi"""
from Prac_08.taxi import Taxi
from Prac_08.Silver_Service_Taxi import SilverTaxi


MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Code to simulate multiple taxis"""
    current_taxi = None
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverTaxi("Limo", 100, 2), SilverTaxi("Hummer", 200, 4)]
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            print_taxis(taxis)
            car_choice = get_valid_integer("Choose Taxi: ")
            while car_choice < 0 or car_choice > len(taxis) - 1:
                print(f"Choice must be between 0 and {len(taxis) - 1}")
                car_choice = get_valid_integer("Choose Taxi: ")
            current_taxi = taxis[car_choice]
            print(f"Bill to date ${total_bill}")
            print(MENU)
            choice = input(">>>").upper()
        if choice == "D":
            if current_taxi is None:
                print("You do not have a taxi selected")
                choice = input(">>>").upper()
            else:
                drive_distance = get_valid_integer("Drive how far? ")
                while drive_distance < 0:
                    print(f"Choice must be above 0")
                    drive_distance = get_valid_integer("Drive how far? ")
                current_taxi.drive(drive_distance)
                total_bill += current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost ${current_taxi.get_fare()}")
                print(MENU)
                choice = input(">>>").upper()
        else:
            if choice != "Q":
                print("You must choose q,d or c")
                print(MENU)
                choice = input(">>>").upper()
    print(f"Total trip cost: ${total_bill}")
    print("Taxis are now")
    print_taxis(taxis)


def print_taxis(taxis):
    """Prints taxis"""
    for value, name in enumerate(taxis):
        print(f"{value} - {name} ")


def get_valid_integer(prompt):
    """Function to make sure input is an integer"""
    valid_input = False
    while not valid_input:
        try:
            car_choice = int(input(prompt))
            return car_choice
        except ValueError:
            print("Choice must be an integer")


main()
