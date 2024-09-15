def func():
    global L, x1, v1, x2, v2
    k = 0
    t1 = -1
    t2 = -1

    if x1 == x2 or x1 + x2 == L:
        print("YES")
        return 0

    if v1 == v2 == 0:
        print("NO")
        return -1
    if v1 - v2 != 0:
        if x2 - x1 <= 0 and v1 - v2 < 0 or x2 - x1 > 0 and v1 - v2 > 0:
            k = 0
            t1 = (x2 - x1 + L * k) / (v1 - v2)
        elif x2 - x1 > 0 and v1 - v2 < 0:
            k = -1
            t1 = (x2 - x1 + L * k) / (v1 - v2)
        elif x2 - x1 <= 0 and v1 - v2 >= 0:
            k = 1
            t1 = (x2 - x1 + L * k) / (v1 - v2)

    if v1 + v2 == 0 and t1 > 0:
        print("YES")
        return t1
    if v1 + v2 != 0:
        if 0 < x2 + x1 < L and v1 + v2 < 0:
            k = -1
            t2 = (L * (k + 1) - x2 - x1) / (v1 + v2)
        elif L < x2 + x1 < 2 * L and v1 + v2 < 0 or 0 < x2 + x1 < L and v1 + v2 > 0:
            k = 0
            t2 = (L * (k + 1) - x2 - x1) / (v1 + v2)
        elif L < x2 + x1 < 2 * L and v1 + v2 > 0:
            k = 1
            t2 = (L * (k + 1) - x2 - x1) / (v1 + v2)

    if t1 < 0 and t2 < 0:
        print("NO")
        return -1
    elif t1 > 0 and t2 < 0:
        print("YES")
        return t1
    elif t1 < 0 and t2 > 0:
        print("YES")
        return t2
    else:
        print("YES")
        return min(t1, t2)


L, x1, v1, x2, v2 = map(int, input().split())
t = func()

if t != -1:
    print(t)