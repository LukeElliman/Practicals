"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """Contains the main program"""
    score = float(input("Enter score: "))
    print(result(score))


def result(score):
    """Determines the users result based on score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif 90 > score >= 50:
        return "Passable"
    else:
        return "Bad"


main()


