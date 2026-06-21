import random

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

length = int(input("How many characters password should be: "))

def pass_generator(length):
    password = ""
    full_password = numbers + U_letters + L_letters + S_symbols

    for i in range(length):
        r_chars = random.choice(full_password)
        password = password + r_chars
    
    print(password)
    return password


pass_generator(length)

