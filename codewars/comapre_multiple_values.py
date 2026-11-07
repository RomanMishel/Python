def expression_matter(a, b, c):
    opt_1 = a + b + c
    opt_2 = (a + b) * c
    opt_3 = a * (b + c)
    opt_4 = a * b * c
    opt_5 = a * b + c
    opt_6 = a + b * c
    
    return max(opt_1, opt_2, opt_3, opt_4, opt_5, opt_6)