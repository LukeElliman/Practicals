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
    word_format = is_valid_format()
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word + "\n")

    #Random
    number_of_letters = int(input("How many letters do you want? "))
    letters = "cv"
    word_format = "".join(random.choice(letters) for i in range(number_of_letters))
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)


def is_valid_format():
    valid_input = False
    while not valid_input:
        valid_character_count = 0
        user_input = str(input("Enter c's for consonant and v's for vowels: ")).lower()
        for each_character in user_input:
            if each_character not in VALID_INPUT:
                valid_character_count += 1
        if valid_character_count > 0:
            print("Your input must only be c's and v's")
        elif len(user_input) <= 0:
            print("Your input must have more then 0 characters")
        else:
            print("Valid input \n")
            valid_input = True
    return user_input

main()