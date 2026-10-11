def well(x):
    good_i = 0
    for i in x:
        if i == "good":
            good_i += 1
                            
    if good_i >= 3:
        return "I smell a series!"
    
    elif good_i == 1 or good_i == 2:
        return "Publish!"
    else:
        return "Fail!"