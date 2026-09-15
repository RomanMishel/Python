numbers = [1,1,1,2,3,2,3,5,4,2,3,1,5,3,2,4,6,6,5,1,6,7]

previous_num = numbers[0]
number_count = 1
max_count = 1

for x in numbers[1:]:
    if x == previous_num:
        number_count += 1
    else:
        number_count = 1

    if number_count > max_count:
        max_count = number_count

    previous_num = x

print("Самая длинная серия:", max_count)