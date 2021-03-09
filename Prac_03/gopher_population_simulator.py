"""
Gopher population simulator
Luke Elliman
"""

import random


MIN_INCREASE = 0.1
MAX_INCREASE = 0.2

MIN_DECREASE = 0.05
MAX_DECREASE = 0.25

YEARS = 10

def main():
    """Runs the main program"""
    population = 1000
    print("Welcome to the Gopher Population Simulator!")
    print("Starting population: {0}".format(population))
    print("Year 1\n")
    for i in range(2, YEARS + 1, 1):
        print(i)



def increase():
    """Generates the increase amount"""
    increase_amount = random.uniform(MIN_INCREASE, MAX_INCREASE)
    return increase_amount


def decrease():
    """Generates the decrease amount"""
    decrease_amount = random.uniform(MIN_DECREASE, MAX_DECREASE)
    return decrease_amount


def population_increase_calculator(population):
    """Calculates the population increase"""
    population = population * decrease()
    return population


def population_decrease_calculator(population):
    """Calculates the population decrease"""
    population = population * decrease()
    return population


main()