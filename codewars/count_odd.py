def odd_count(n):
    list_item = []
    for x in range(n):
        if x != 0:
            new_n = n // 2
            if new_n == 1:
                list_item.append(new_n)
    return new_n