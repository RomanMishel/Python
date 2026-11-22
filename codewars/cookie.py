def cookie(x):
    typed = type(x)
    if typed == str:
        return "Who ate the last cookie? It was Zach!"
    elif typed == int:
        return "Who ate the last cookie? It was Monica!"
    elif typed == float:
        return "Who ate the last cookie? It was Monica!"
    else:
        return "Who ate the last cookie? It was the dog!"