from random import choice

def hangman():
    wordlist = ["cat", "milk", "python", "hangman", "computer"]
    word_to_guess = choice(wordlist)

    display_word = ["_"] * len(word_to_guess)

    print("Welcome to Hangman!")
    print(" ".join(display_word))

    while "_" in display_word:
        user_guess = input("Guess a letter: ")

        for index, letter in enumerate(word_to_guess):
            if letter == user_guess:
                display_word[index] = user_guess

        print(" ".join(display_word))
    print("You win")

hangman()
        

