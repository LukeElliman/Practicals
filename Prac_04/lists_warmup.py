numbers = [3, 1, 4, 1, 5, 9, 2]

print(numbers[0])   #3
print(numbers[-1])  #2
print(numbers[3])   #1
print(numbers[:-1]) #3, 1, 4, 1, 5, 9
print(numbers[3:4]) #1
print(5 in numbers) #true
print(7 in numbers) #false
print("3" in numbers) #false
print(numbers + [6, 5, 3]) #[3, 1, 4, 1, 5, 9, 2, 6, 5, 3]