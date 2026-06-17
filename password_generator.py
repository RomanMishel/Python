import random

global password 
password = ""

user_input = int(input("How many characters password should be: "))

numbers = [
    "1","2","3","4","5","6","7","8","9","0"
    ]

U_letters = [
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
]

L_letters = small_letters = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
]

S_symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*",
    "(", ")", "-", "_", "=", "+",
    "[", "]", "{", "}","|",
    ";", ":", "<", ">", "/","?", "~"
]

def pass_generator(length={user_input}):
    
    for i in range(user_input):
        r_num = random.choice(numbers)
        r_letter = random.choice(U_letters + L_letters)
    
    password = password + r_num + r_letter
    print(password)
    return
pass_generator()
