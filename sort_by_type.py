list = [42, -7, 3.14, True, False, "hello"]
int_items = []
float_items = []
bool_items = []
str_items = []

for x in list:
    if type(x) == int:
        int_items.append(x)
    elif type(x) == float:
        float_items.append(x)
    elif type(x) == bool:
        bool_items.append(x)
    elif type(x) == str:
        str_items.append(x)
    else:
        print("Error")

print(f"{int_items}\n{float_items}\n{bool_items}\n{str_items}")
        