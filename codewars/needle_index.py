def find_needle(haystack):
    for x in haystack:
        if x == "needle":
            Index_x = haystack.index(x)
            return f"found the needle at position {Index_x}"