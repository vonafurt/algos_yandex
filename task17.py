import sys


def func():
    n = int(input())
    a = list(map(int, input().split()))
    lens = []
    length = 0
    max_len = a[0]
    minimum = max_len
    for j in range(n):
        if a[j] < minimum:
            minimum = a[j]
            max_len = a[j]

        if length >= max_len:
            lens.append(length)
            length = 1
            minimum = a[j]
            max_len = a[j]
        else:
            length += 1
    lens.append(length)
    print(len(lens))
    for j in range(len(lens)):
        print(lens[j], ' ', end='')
    print()


r = int(input())

for i in range(r):
    func()
