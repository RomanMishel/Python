def century(year):
    full_centuries = year // 100
    end_cent = year % 100
    if end_cent == 0:
        return full_centuries
    else:
        return full_centuries +1