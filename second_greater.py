first_input = input("Enter a digit: ")
second_input = input("Enter a digit: ")

if first_input > second_input:
    print(f"{first_input} is the second greater number")
elif first_input < second_input:
    print(f"{second_input} is the second greater number")

else:
    print("Error")