#Program 1
import random
print("Program 1")
random_number = random.randint(0,1)
boolean_one = bool(random_number)
print("The result is {}".format(boolean_one))

#Program 2
print("Program 2")
boolean_two = random.choice([True,False])
print("The result is {}".format(boolean_two))

#Program 3
print("Program 3")
random_bit = random.getrandbits(1)
boolean_three = bool(random_bit)
print("The result is {}".format(boolean_three))
