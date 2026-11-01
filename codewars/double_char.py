def double_char(s):
    new_x = ""
    new_string = ""
    for x in s:
        new_x = x + x
        new_string = new_string + new_x
    return new_string