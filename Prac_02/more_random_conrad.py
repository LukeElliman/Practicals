"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = random.uniform(0,0.5)  # 17.5%
MAX_DECREASE = random.uniform(0,0.5)
MIN_PRICE = random.uniform(0,9)
MAX_PRICE = random.uniform(50,100)
INITIAL_PRICE = random.uniform(10,20)
OUTPUT_FILE = "stock_ouput_random.txt"

day = 0
price = INITIAL_PRICE

out_file = open(OUTPUT_FILE, 'w')

print("Max increase is {:,.2f}%, Max decrease is {:,.2f}%, Min price is ${:,.2f}, Max price is ${:,.2f}".format(100 * MAX_INCREASE, 100 * MAX_DECREASE, MIN_PRICE, MAX_PRICE), file=out_file)
print("On day {} the price is: ${:,.2f}".format(day, price), file=out_file)

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    day += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("On day {} the price is: ${:,.2f}".format(day, price), file=out_file)

out_file.close()