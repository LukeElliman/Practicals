"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """Contains the main program"""
    score = float(input("Enter score: "))
    print(result_determine(score))
    score = random_score()
    print("{0} is {1}".format(score, result_determine(score)))


def result_determine(score):
    """Determines the users result based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif 90 > score >= 50:
        return "Passable"
    else:
        return "Bad"


def random_score():
    random_value = random.randint(0,100)
    return random_value


main()


