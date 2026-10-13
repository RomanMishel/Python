def invert(lst):
    new_lst = []
    for n in lst:
        if n > 0:
            n = n * (-1)
            new_lst.append(n)
        elif n < 0:
            n = n * (-1)
            new_lst.append(n)
        else:
            new_lst.append(0)
    return new_lst