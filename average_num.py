def average_num():

    print("Type at least 5 numbers to calculate the average number.")
    num_a = int(input("Type first number: "))
    num_b = int(input("Type second number: "))
    num_c = int(input("Type third number: "))
    num_d = int(input("Type fourth number: "))
    numb_e = int(input("Type fifth number: "))

    total_num = [num_a, num_b, num_c, num_d, numb_e]
    av_num = sum(total_num) / len(total_num)
    print(f"Your average number is {av_num}!")

average_num()
