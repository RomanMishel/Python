def neutralise(s1, s2):
    result = ""
    
    for x, y in zip(s1, s2):
        if x == y:
            result += x
        else:
            result += "0"
    return result
    