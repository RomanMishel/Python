user_input = int(input("Enter a number: "))

fractal = 1

for n in range(1,user_input + 1):
    fractal = fractal * n

print(fractal)
