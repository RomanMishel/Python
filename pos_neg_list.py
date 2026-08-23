num_list = [5, -8, 2, -9 , 1, -1, -3, -5, 3]
pos_list = []
neg_list = []

for num in num_list:
    if num > 0:
        pos_list.append(num)
    elif num < 0:
        neg_list.append(num)

    else:
        print("Error")
        
print(pos_list)
print(neg_list)