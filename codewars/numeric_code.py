def validate_code(code):
    integer = str(code)
    f_int = integer[0]
    if f_int == "1" or f_int == "2" or f_int == "3":
        return True
    
    else:
        return False