import sys

n = int(input())
a = [0] * n
for i in range(0, n):
    a[i] = list(map(int, input().split()))

maxy = -sys.maxsize
maxx = -sys.maxsize
miny = sys.maxsize
minx = sys.maxsize

for i in range(n):
    if a[i][0] > maxx:
        maxx = a[i][0]
    if a[i][0] < minx:
        minx = a[i][0]
    if a[i][1] > maxy:
        maxy = a[i][1]
    if a[i][1] < miny:
        miny = a[i][1]

print(minx, miny, maxx, maxy)