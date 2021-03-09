"""
Gopher population simulator
Luke Elliman
"""

import random

INITIAL_POPULATION = 1000

MIN_INCREASE = 0.1
MAX_INCREASE = 0.2

MIN_DECREASE = 0.05
MAX_DECREASE = 0.25


def main():
    """Runs the main program"""


def increase():
    increase_amount = random.uniform(MIN_INCREASE, MAX_INCREASE)
    return increase_amount


def decrease():
    decrease_amount = random.uniform(MIN_DECREASE, MAX_DECREASE)
    return decrease_amount


main()