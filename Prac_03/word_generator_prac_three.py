"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def main():
    #User input
    word_format = str(input("Enter c's for consonant and v's for vowels: ")).lower()
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)
    print()

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


main()