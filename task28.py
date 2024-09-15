import time

n = int(input())
t = time.time()

count = 0
k = 0

#x = (n / 0.21214034061399408837) ** (1 / 2.96837056560548795403)
#y=0.18311672491662811524x^2.98964456464152794624
x = (n / 0.18311672491662811524) ** (1 / 2.98964456464152794624)
#х - какой длины примерно будет самый длинный корабль
x = round(x)
#k - количество клеток
for i in range(x):
    k += (i + 1) * (x - i)
    count += i + 1
k += count - 1
if n >= k:
    while n >= k:
        x += 1
        for i in range(x):
            k += (i + 1) + 1
        k -= 1
    print(x - 1)
else:
    while n <= k:
        for i in range(x):
            k -= (i + 1) + 1
        k -= 1
        x -= 1
    print(x)
print(time.time() - t)

k = 0
count = 0
'''
while k <= n:
    k = 0
    for i in range(count):
        k += (i + 1) * (count - i + 1)
    k -= 1
    count += 1
    #print('(', count - 1,', ', k,')')
    print(k, end=' ')
    #print(k / (count - 1))
'''