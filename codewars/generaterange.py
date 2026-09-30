def generate_range(start, stop, step):
    new_list = []
    for x in range(start, stop +1, step):
        new_list.append(x)
    return new_list