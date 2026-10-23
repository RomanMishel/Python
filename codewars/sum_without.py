def sum_array(arr):
    if arr is None or len(arr) < 3:
        return 0
    new_arr = arr
    
    x = min(new_arr)
    y = max(new_arr)
    
    new_arr.remove(x)
    new_arr.remove(y)
    
    return sum(new_arr)