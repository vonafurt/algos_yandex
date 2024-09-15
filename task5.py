def func(k, n, d):
    flag = 0
    for i in range(0, 10):
        if (k * 10 + i) % n == 0:
            k = k * 10 + i
            flag = 1
            break
    if flag == 0:
        return -1
    print(k, end="")
    for i in range(0, d - 1):
        print(0, end="")
    return k


k, n, d = map(int, input().split())
ans = func(k, n, d)
if ans == -1:
    print(ans)
