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
            car_choice = get_valid_integer("Choose Taxi: ", taxis)
            current_taxi = taxis[car_choice]
            print(f"Bill to date ${total_bill}")
            print(MENU)
            choice = input(">>>").upper()
        if choice == "D":
            if current_taxi is None:
                print("You do not have a taxi selected")
                choice = input(">>>").upper()
            else:
                drive_distance = get_valid_integer("Drive how far? ", taxis)
                print(current_taxi)
                current_taxi.drive(drive_distance)

        else:
            print("You must choose q,d or c")
            print(MENU)
            choice = input(">>>").upper()


def print_taxis(taxis):
    """Prints taxis"""
    for value, name in enumerate(taxis):
        print(f"{value} - {name} ")


def get_valid_integer(prompt, taxis):
    """Function to make sure input is an integer"""
    valid_input = False
    while not valid_input:
        try:
            car_choice = int(input(prompt))
            if car_choice > len(taxis) - 1 or car_choice < 0:
                print(f"Choice must be between 0 and {len(taxis) - 1}")
            else:
                return car_choice
        except ValueError:
            print("Choice must be an integer")


main()
