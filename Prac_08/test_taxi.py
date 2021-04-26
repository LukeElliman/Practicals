"""Taxi test"""
from Prac_08.taxi import Taxi


def main():
    """Code to test a taxi"""
    prius_one = Taxi("Pirus 1", 100, 1.23)
    prius_one.drive(40)
    print(prius_one)
    prius_one.start_fare()
    prius_one.drive(100)
    print(prius_one)


main()