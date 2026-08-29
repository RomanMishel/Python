user_choice = input("1.Seconds to Minutes\n2.Minutes to Seconds\nPlease choose the coverter: ")
user_input = int(input("Enter a number please: "))

if user_choice == "1":
    Minutes = float(user_input / 60)
    print(f"{user_input} seconds is a {Minutes:.2f} minutes")

elif user_choice == "2":
    Seconds = user_input * 60
    print(f"{user_input} minutes is {Seconds} seconds")