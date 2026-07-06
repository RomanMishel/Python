from random import choice, random

def hangman():
    wordlist = ["cat", "milk", "python", "hangman", "computer"]
    word_to_guess = random.choice(wordlist)
    length_of_word = len(word_to_guess)
    print("Welcome to Hangman!")
    print("_" * length_of_word)

    