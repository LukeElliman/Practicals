for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

star_count = int(input("How many stars do you want? "))
for i in range(0, int(star_count), 1):
    print(end=' *')
print()

increasing_stars = int(input("How many stars do you want? "))
for i in range(1, int(increasing_stars) + 1, 1):
    print(i * "*")
print()