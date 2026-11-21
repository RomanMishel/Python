def smash(words):
    sentence = ''
    for i in words:
        sentence = sentence + i + " "
    return sentence.rstrip()