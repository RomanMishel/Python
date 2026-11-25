def array_madness(a,b):
    sum_a = 0
    sum_b = 0
    for n in a:
        n = n * n
        sum_a = sum_a + n
    for x in b:
        x = x * x * x
        sum_b = sum_b + x
    
    if sum_a > sum_b:
        return True
    else:
        return False