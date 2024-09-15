import sys
from copy import deepcopy

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

b = deepcopy(a)

maxim = -sys.maxsize
raw = -1
string = -1

for i in range(n):
    for j in range(m):
        if a[i][j] > maxim:
            maxim = a[i][j]
            string = i
            raw = j
for i in range(max(m, n)):
    if i < m:
        a[string][i] = 0
    if i < n:
        b[i][raw] = 0

maxim = -sys.maxsize
maxim1 = -sys.maxsize
b_raw = raw
a_string = string

for i in range(n):
    for j in range(m):
        if a[i][j] > maxim:
            maxim = a[i][j]
            raw = j
        if b[i][j] > maxim1:
            maxim1 = b[i][j]
            string = i
for i in range(max(n, m)):
    if i < n:
        a[i][raw] = 0
    if i < m:
        b[string][i] = 0

maxim = -sys.maxsize
maxim1 = -sys.maxsize

for i in range(n):
    for j in range(m):
        if a[i][j] > maxim:
            maxim = a[i][j]
        if b[i][j] > maxim1:
            maxim1 = b[i][j]

if maxim < maxim1:
    print(a_string + 1, raw + 1)
else:
    print(string + 1, b_raw + 1)