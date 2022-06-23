def math():

    list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    newlist = []
    counter = 0

    while counter != 90:
        if counter in list1 and counter in list2:
            newlist.append(counter)

        counter += 1
    return newlist


a = math()
print(a)