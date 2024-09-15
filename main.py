p, v = map(int, input().split())
q, m = map(int, input().split())
if v < 0 and m < 0:
    print(0)
elif v < 0:
    print(2 * m + 1)
elif m < 0:
    print(2 * v + 1)
elif abs(p - q) + v <= m or abs(p - q) + m <= v:
    print(2 * max(m, v) + 1)
elif abs(p - q) <= m + v:
    print(m + v + abs(p - q) + 1)
else:
    print(2 * m + 2 * v + 2)