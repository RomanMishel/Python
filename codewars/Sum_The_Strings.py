def sum_str(a: str, b: str) -> str:
    if a == "" and b == "":
        return "0"
    elif a == "" and b != "":
        return f"{b}"
    elif a != "" and b == "":
        return f"{a}"
    else:
        num_1 = int(a)
        num_2 = int(b)
        sum_item = num_1 + num_2
        return f"{sum_item}"