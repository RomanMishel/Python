from random import choice

def hangman():
    wordlist = ["cat", "milk", "python", "hangman", "computer"]
    word_to_guess = choice(wordlist)
    length_of_word = len(word_to_guess)
    print("Welcome to Hangman!")
    print("_" * length_of_word)

    user_guess = input("Guess a letter: ")

    while True:
        for index, letter in enumerate(word_to_guess):
            display_word[index] = user_guess
            print(" ".join(display_word))

hangman()
        

