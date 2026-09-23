def set_alarm(employed, vacation):
    if employed and not vacation:
        return True
    elif employed and vacation:
        return False
    elif not employed:
        return False
    else:
        return True