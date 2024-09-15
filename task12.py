n, k = map(int, input().split())
a = list(map(int, input().split()))

maximum = 0

for i in range(n):
    for j in range(1, k + 1):
        if i + j >= n:
            break
        if a[i + j] - a[i] > maximum:
            maximum = a[i + j] - a[i]

print(maximum)