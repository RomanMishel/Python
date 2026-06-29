def password_checker(user_input):
    has_upper_case = any(char.isupper() for char in user_input)
    has_digits = any(char.isdigit() for char in user_input)
    has_symbols = any(char.isalnum() for char in user_input)

    if has_upper_case and has_digits and has_symbols and len(user_input) >= 8:
        print("You password is Strong!")
        return True
    else:
        print("Your password is weak!")
        return False

user_input = input("Enter you password to check: ")

password_checker(user_input)

