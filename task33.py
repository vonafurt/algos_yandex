with open("input.txt", "r") as f:
    n, k = map(int, f.readline().split())
    v = [0]
    line = list(map(int, f.readline().split()))
    for i in range(n):
        v.append(v[-1] + line[i])

    for _ in range(k):
        size, target_sum = map(int, f.readline().split())
        l1, r1 = 1, n - size + 1
        tmp = 0
        while l1 < r1:
            m = (l1 + r1) // 2
            if v[m + size - 1] - v[m - 1] < target_sum:
                l1 = m + 1
            else:
                r1 = m
        if v[l1 + size - 1] - v[l1 - 1] == target_sum:
            tmp = v[l1 + size - 1] - v[l1 - 1]
        print(l1 if tmp > 0 else -1)