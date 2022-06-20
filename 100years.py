year_now = 2022
name = input('Enter your name: ')
print(name)
age = int(input('Enter your age: '))
print(age)

print(type(year_now),type(age))

yearwhen = year_now - age + 100

print(f'You are {name} and you will turn 100 in {yearwhen} year')