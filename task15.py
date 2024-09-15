import functools

import sys
import time


def solve():
    n = int(input())
    berries = [[0, 0] for _ in range(n)]
    for i in range(n):
        x, y = map(int, input().split())
        berries[i][0] = x
        berries[i][1] = y
    t = time.time()
    climb_len = []
    for i in range(n):
        a = berries[i][0]
        b = berries[i][1]
        climb_len.append([a - b, a, b, i])
    # climb_len = sorted(climb_len, key=lambda x: x[0], reverse=True)
    # print(climb_len)
    ans = 0
    good = [i for i in climb_len if i[0] > 0]
    bad = [i for i in climb_len if i[0] <= 0]
    #good.sort(key=lambda x: x[2], reverse=False)
    bad.sort(key=lambda x: x[1], reverse=True)
    if len(good) == 0:
        print(bad[0][1])
        print(*[i[3] + 1 for i in bad])
        return
    for i in good:
        ans += i[0]

    lastgoodind = -1337
    lastgoodvalue = -2e9

    for ind, i in enumerate(good):
        if i[2] > lastgoodvalue or (i[2] == lastgoodvalue and (lastgoodind == -1337 or good[lastgoodind][1] < i[1])):
            lastgoodvalue = i[2]
            lastgoodind = ind

    good[-1], good[lastgoodind] = good[lastgoodind], good[-1]

    if len(bad) == 0:
        print(ans + good[-1][2])
        print(*[i[3] + 1 for i in good])
        return
    print(max(ans + bad[0][1], ans + good[-1][2]))
    print(*[i[3] + 1 for i in good])
    print(*[i[3] + 1 for i in bad])


solve()
