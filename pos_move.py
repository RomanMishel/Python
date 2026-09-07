numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_input = int(input("Enter a number of positions to move: "))

result = numbers[-user_input:] + numbers[:-user_input]

print(result)  # [4, 5, 1, 2, 3]