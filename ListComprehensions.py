var1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = []
for num in var1:
    new_num = num / 2
    if round(new_num) == new_num:
        new_list.append(new_num)

print(new_list)
