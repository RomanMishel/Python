list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = int(input('Enter number: '))
list2 = []
for i in list1:

    num1 = a / i


    if round(num1) != num1:
        print('Cant divide by ', (i))
    else:
        print("Can divide by ", (i))