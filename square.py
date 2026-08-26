width = int(input("Enter a weight of square: "))
height = int(input("Enter a height of a square: "))
symbol = input("Enter a symbol: ")

for row in range(height):
    print(symbol * width)