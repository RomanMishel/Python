def polygon_area(a, b, c, d):
    walls_area = b * a
    roof_height = c - a
    roof_area = b * roof_height / 2
    return walls_area + roof_area