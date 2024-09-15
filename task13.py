def func(lens):
    maxlen = max(lens)
    maxlen_index = lens.index(maxlen)
    otherlen = 0 # длина всех веревок кроме самой большой
    for i in range(len(lens)):
        if i != maxlen_index:
            otherlen += lens[i]
    if maxlen > otherlen:
        return maxlen - otherlen
    else:
        return maxlen + otherlen

n = int(input())
lens = list(map(int, input().split())) # длины веревочек

print(func(lens))