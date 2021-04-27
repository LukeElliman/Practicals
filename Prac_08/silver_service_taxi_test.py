"""Silver Service Taxi Testing"""

from Prac_08.Silver_Service_Taxi import SilverTaxi


def main():
    """Code to test silver service taxi class"""
    car_fanciness_two = SilverTaxi("Fanciness_two", 200, 2)
    print(car_fanciness_two)
    car_fanciness_two.drive(18)
    print(car_fanciness_two)
    print(f"${car_fanciness_two.get_fare()}")

main()
