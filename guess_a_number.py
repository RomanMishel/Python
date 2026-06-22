import random

num_list = [
    1,2,3,4,5,6,7,8,9
]

user_input = int(input("Guess a number: "))

def guess(user_input):
    random_num = random.choice(num_list)
    

    if random_num < user_input:
        print("You guessed wrong, you number is too high")
        print(random_num)
        return 
    elif random_num > user_input:
        print("You guessed wrong, you number is too low")
        print(random_num)
        return 
    elif random_num == user_input:
        print("You guessed right!")
        print(random_num)
        return 
    else:
        print("error")
        return

guess(user_input)