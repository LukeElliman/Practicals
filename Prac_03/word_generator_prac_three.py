"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
VALID_INPUT = "cv"


def main():
    #User input
    valid_input = False
    while not valid_input:
        word_format = str(input("Enter c's for consonant and v's for vowels: ")).lower()
        valid_input = is_valid_format(word_format)
    word = word_generator(word_format)

    print(word + "\n")

    #Random
    number_of_letters = int(input("How many letters do you want? "))
    letters = "cv"
    word_format = "".join(random.choice(letters) for i in range(number_of_letters))
    word = word_generator(word_format)

    print(word)


def is_valid_format(user_input):
    """Checks if input is valid"""
    valid = False
    valid_character_count = 0
    for each_character in user_input:
        if each_character not in VALID_INPUT:
            valid_character_count += 1
    if valid_character_count > 0:
        print("Your input must only be c's and v's")
        valid_character_count = 0
    elif len(user_input) <= 0:
        print("Your input must have more then 0 characters")
    else:
        print("Valid input \n")
        valid = True
    return valid


def word_generator(user_input):
    """Turns the cv input into words"""
    word = ""
    for kind in user_input:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)
    return word


main()