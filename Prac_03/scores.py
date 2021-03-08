"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """Contains the main program"""
    number_of_scores = score_choice_amount()
    print(number_of_scores)


def score_choice_amount():
    valid_number = False
    while not valid_number:
        try:
            value = int(input("How many scores do you want? "))
            if value <= 0:
                print("The value must be above 0")
            else:
                valid_number = True
        except ValueError:
            print("You must input an integer")
    return value


# def result_determine(score):
#     """Determines the users result based on score"""
#     if score < 0 or score > 100:
#         return "Invalid score"
#     elif score >= 90:
#         return "Excellent"
#     elif 90 > score >= 50:
#         return "Passable"
#     else:
#         return "Bad"
#
#
# def random_score():
#     """Generates a random value between 0 to 100"""
#     random_value = random.randint(0, 100)
#     return random_value


main()