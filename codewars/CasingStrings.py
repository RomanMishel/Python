def to_jaden_case(string):
    for word in string:
        string = " ".join(word.capitalize() for word in string.split())
    return string