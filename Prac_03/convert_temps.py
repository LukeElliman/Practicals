"""
Program to generate a file containing fahrenheit values to celsius
Luke Elliman
"""

import random

MIN_FAHRENHEIT = -200
MAX_FAHRENHEIT = 200


def main():
    """Converts text file with fahrenheit values to celsius values"""
    #random_fahrenheit_list(15)
    in_file = open("temps_input.txt", "r")
    out_file_celsius = open("temps_output.txt", "w")
    for line in in_file:
        celsius = fahrenheit_to_celsius(float(line))
        print("{0}".format(celsius), file=out_file_celsius)
    in_file.close()
    out_file_celsius.close()


def random_fahrenheit_list(amount):
    """Generates a random list of values in a text file"""
    out_file = open("temps_input.txt", "w")
    for i in range(amount):
        print(random.uniform(MIN_FAHRENHEIT, MAX_FAHRENHEIT), file=out_file)
    out_file.close()


def fahrenheit_to_celsius(fahrenheit):
    """Converts fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()