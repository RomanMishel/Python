def battery_bars(percent):
    if percent == 100:
        return "[#####]"
    elif percent >= 80 and percent <= 99:
        return "[####.]"
    elif percent >= 60 and percent <= 79:
        return "[###..]"
    elif percent >= 40 and percent <= 59:
        return "[##...]"
    elif percent >= 20 and percent <= 39:
        return "[#....]"
    else:
        return "[.....]"