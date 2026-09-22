def zero_fuel(distance_to_pump, mpg, fuel_left):
    distance_to_pump = distance_to_pump - mpg * fuel_left
    if distance_to_pump <= 0:
        return True
    else:
        return False