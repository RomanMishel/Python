def palindrome():
    user_word = input("Enter your word to check if its palindrome: ")

    if user_word == user_word[::-1]:
        print("This word is palindrome!")

    else:
        print("This word is not palindrome!")

palindrome()