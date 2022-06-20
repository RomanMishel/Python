def fibn_s(n):
    x = 0
    y = 1

    if n == 1:
        print(x)

    else:
        print(x)
        print(y)

        for i in range(n - 2):
            num1 = x + y
            x = y
            y = num1
            print(num1)


fibn_s(10)