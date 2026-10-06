def odd_or_even(arr):
    new_sum = sum(arr)
    x = new_sum % 2
    if x == 0:
        return "even"
    else:
        return "odd"