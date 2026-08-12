x_side = 0
y_side = 0
z_side = 0

x = int(input("Enter a X length: "))
x_side = x

y = int(input("Enter a Y length: "))
y_side = y

z = int(input("Enter a Z length: "))
z_side = z


if x_side <= 0 or y_side <= 0 or z_side <= 0:
    print("Sides must be greater than zero")

elif (
    x_side + y_side <= z_side
    or x_side + z_side <= y_side
    or y_side + z_side <= x_side
):
    print("Triangle does not exist")

elif x_side == y_side == z_side:
    print("Triangle is equilateral")

elif x_side == y_side or x_side == z_side or y_side == z_side:
    print("Triangle is isosceles")

else:
    print("Triangle is scalene")