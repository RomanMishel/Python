x_side = 0
y_side = 0
z_side = 0

x = int(input("Enter a X length: "))
x_side = x

y = int(input("Enter a Y length: "))
y_side = y

z = int(input("Ener a Z length: "))
z_side = z

if x_side or y_side or z_side == 0:
    print("Sides cannot be equal to 0")
    
else:
    if x_side == y_side == z_side:
        print("Triangle is equal")

    elif x_side == y_side < z_side:
        print("Triangle sides unequal ")

    elif x_side == y_side > z_side:
        print("Triangle sides unproper")

    elif x_side > y_side > z_side:
        print("Sides are different")

    elif x_side < y_side > z_side:
        print("Sides are different")

    else:
        print("Error")