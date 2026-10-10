def lovefunc( flower1, flower2 ):
    total_pestals = flower1 + flower2
    total_pestals = total_pestals % 2
    if total_pestals == 0:
        return False
    else:
        return True