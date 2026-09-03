words_list = ["elephant", "cat" , "leopard", "shark"]

shortest = words_list[0]

for w in words_list:
    word_len = len(w)

    if word_len < len(shortest):
        shortest = w

print(shortest)