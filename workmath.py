def work_math():
    a7 = int(input("сколько дней по 7 часов?: " ))
    a7 = a7 * 7
    b8 = int(input("сколько дней по 8 часов?: " ))
    b8 = b8 * 8
    print(f'часов по 7 часовой: {a7}')
    print(f'часов по 8 часовой: {b8}')
    a7_money = a7 * 38
    b8_money = b8 * 38
    print(a7_money)
    print(b8_money)
    shabat_money = int(input("сколько шабатных часов?: "))
    tosefet = 38 * 0.5
    shabat_money = shabat_money * (int(38 + tosefet))
    print(f'деньги от шабата {shabat_money}')
    result = a7_money + b8_money + shabat_money
    print(f'зарплата будет примерно {result}')
work_math()  
    

    