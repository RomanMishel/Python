def positive_sum(arr):
    new_array = [0]
    for x in arr:
        if x > 0:
            new_array.append(x)
    return sum(new_array)