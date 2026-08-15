def temp_converter():
    print("1.Celsius to Fahrenheit\n2.Fahrenheit to Celsius")
    user_input = int(input("Please choose an option:"))

    if user_input == 1:
        user_num = float(input("Enter a temperature: "))
        converted_f = user_num * 1.8 + 32
        print(f"{user_num} °C is {converted_f} °F")

    elif user_input == 2:
        user_num = float(input("Enter a temperature: "))
        converted_c = (user_num - 32) / 1.8
        print(f"{user_num} °F is {converted_c:.2f} °C")
    else:
        print("Error")
        return

temp_converter()
