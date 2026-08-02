def simple_reg():
    print("Welcome to registration page!")
    user_name = input("Please Enter your Username: ")
    user_pass = input("Please Enter your Password: ")

    user_input = input("To Sign In please Enter your username: ")
    user_input_pass = input("Enter your password please: ")
    
    if user_input and user_input_pass == user_name and user_pass:
        print("Welcome to your account!")
        print("You just signed in!")
    else:
        print("Username or Password is incorrect!")
        return

simple_reg()