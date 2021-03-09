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
    for year in range(2, YEARS + 1, 1):
        population_print(population, year)


def increase():
    """Generates the increase amount"""
    increase_amount = random.uniform(MIN_INCREASE, MAX_INCREASE)
    return increase_amount


def decrease():
    """Generates the decrease amount"""
    decrease_amount = random.uniform(MIN_DECREASE, MAX_DECREASE)
    return decrease_amount


def population_increase(population):
    """Calculates the population increase"""
    population = population * decrease()
    return population


def population_decrease(population):
    """Calculates the population decrease"""
    population = population * decrease()
    return population


def population_print(population, value):
    """
    Prints out the increase and decrease in population.
    Then calculates and prints the population at the end of the year
    """
    increase_amount = population_increase(population)
    decrease_amount = population_decrease(population)
    print("{0} gophers were  born. {1} died.".format(int(increase_amount), int(decrease_amount)))
    population = population + int(increase_amount) - int(decrease_amount)
    print("Population: {0}".format(int(population)))
    print("Year {0}\n".format(value))


main()
