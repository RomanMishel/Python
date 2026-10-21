def battery_bars(percent):
    for x in range(0, 100, percent):
        if percent >= 80 and percent <= 100:
            return "[#####]"
        elif percent >= 60 and percent <= 79:
            return "[###..]"
        elif percent >= 40 and percent <= 59:
            return "[##...]"
        elif percent >= 20 and percent <= 39:
            return "[#....]"
        else:
            return "[.....]"