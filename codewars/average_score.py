def better_than_average(class_points, your_points):
    average_class  = sum(class_points) / len(class_points)
    if your_points > average_class:
        return True
    else:
        return False