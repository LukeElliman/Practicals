"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    ValueError occurs when the user enters a value of numerator or denominator that isn't an integer and
    denominator isn't 0
2. When will a ZeroDivisionError occur?
    ZeroDivisionError occurs when the denominator value is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""



try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("The denominator can't be 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
