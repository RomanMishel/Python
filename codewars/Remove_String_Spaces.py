def no_space(x):
    new_items = []
    for i in x:
        if i != " ":
            new_items.append(i)
    return "".join(new_items)
