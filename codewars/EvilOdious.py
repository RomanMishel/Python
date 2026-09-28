def evil(n):
    bin_item = bin(n)
    count = bin_item.count("1")
    count = count % 2
    if count == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"