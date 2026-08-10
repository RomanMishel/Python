def total_num_sum():
    user_input = input("Enter a number: ")
    total = 0

    for digit in user_input:
        total += int(digit)

    print(total)
total_num_sum()
    