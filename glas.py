glas = "aeiouAEIOU"

user_input = input("Enter your sentence: ")

for letter in glas:
    user_input = user_input.replace(letter, "*")

print(user_input)