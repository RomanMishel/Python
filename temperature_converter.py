def temp_converter():
    print("1.Celcius to Fahrenheit\n2.Fahrenheit to Celcius")
    user_input = int(input("Please choose an option:"))

    if user_input == 1:
        user_num = int(input("Enter a temperature: "))
        converterd_f = float(user_num * 1.8 + 32 )
        print(f"{user_num} °C is {converterd_f} °F")

    elif user_input == 2:
        user_num = int(input("Enter a temperature: "))
        converterd_c = float(user_num - 32 / 1.8) 
        print(f"{user_num} °F is {converterd_c:.2f} °C")
    else:
        print("Error")
        return

temp_converter()