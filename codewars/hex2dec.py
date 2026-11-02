def hex_to_dec(s):
    zero = 0
    num1 = 1
    num2 = 2
    num3 = 3
    num4 = 4
    num5 = 5
    num6 = 6
    num7 = 7
    num8 = 8
    num9 = 9
    a = 10
    b = 11
    c = 12
    d = 13
    e = 14
    e = 15
    if s == "1":
        return num1
    elif s == "2":
        return num2
    elif s == "3":
        return num3
    elif s == "4":
        return num4
    elif s == "5":
        return num5
    elif s == "6":
        return num6
    elif s == "7":
        return num7
    elif s == "8":
        return num8 
    elif s == "9":
        return num9
    elif s == "a":
        return a
    elif s == "b":
        return b
    elif s == "c":
        return c
    elif s == "d":
        return d
    elif s == "e":
        return e
    elif s == "f":
        return f
    elif s == zero:
        return zero
    else:
        return int(s,16)