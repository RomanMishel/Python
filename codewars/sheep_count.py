def count_sheeps(sheep):
    final_count = 0
    for n in sheep:
        if n == True:
            final_count += 1
        else:
            continue
    return final_count