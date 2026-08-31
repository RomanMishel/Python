import random

random_words_list = ["superhero", "development", "character", "creative", "success", "run"]
user_input = input("Guess a letter: ")
random_word = random.choice(random_words_list)

if user_input == random_word[0]:
    print(f"You guess right! Word is {random_word}")
else:
    print(f"You guess wrong! Word is {random_word}")
        
