user_number = input("Введите число от 0 до 255: ")
user_number = round(float(user_number))

if  0 > user_number or user_number > 255:
    print("Error! You cannot enter number higher than 255 or negative!")

else:
    binary_number = bin(user_number)[2:].zfill(8)
    print(binary_number)