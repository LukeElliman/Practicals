"""
Program to generate a file containing fahrenheit values to celsius
Luke Elliman
"""

import random


def main():
    random_fahrenheit_list()


def random_fahrenheit_list():
    out_file = open("temp_input.txt", "w")
    for i in range(0, 21, 1):
        print(random.uniform(-200,200), file=out_file)
    out_file.close()


main()