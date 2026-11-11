def logical_calc(array, op):
    item_1 = array[0]
    item_n = array[1:]
    
    for item in item_n:
        if op == "AND":
            item_1 = item_1 and item
            
        elif op == "OR":
            item_1 = item_1 or item
            
        elif op =="XOR":
            item_1 = item_1 != item
    return item_1    