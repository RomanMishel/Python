def sort_num():
    num_list = []
    while len(num_list) != 5:
        user_input = int(input("Enter a digit: "))
        num_list.append(user_input)
        num_list.sort()
    
    print(num_list)
sort_num()
