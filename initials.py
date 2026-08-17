first_name = input("Enter your name: ")
last_name = input("Enter you last name: ")

for initial_first_name in first_name:
    initial_1 = first_name[0].upper()

for initial_last_name in last_name:
    initial_2 = last_name[0].upper()

print(f"Initials for {first_name} {last_name} is {initial_1} {initial_2}")