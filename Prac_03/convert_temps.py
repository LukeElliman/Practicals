"""
Program to generate a file containing fahrenheit values to celsius
Luke Elliman
"""

import random


def main():
    random_fahrenheit_list()


def random_fahrenheit_list():
    """Generates a random list of values in a text file"""
    out_file = open("temps_input.txt", "w")
    for i in range(0, 21, 1):
        print(random.uniform(-200, 200), file=out_file)
    out_file.close()


def fahrenheit_to_celsius(fahrenheit):
    """Converts fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()