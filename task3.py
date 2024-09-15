def func(x):
    if x % 4 == 0:
        return x // 4
    elif x % 4 == 1:
        return x // 4 + 1
    elif x % 4 == 2:
        return x // 4 + 2
    else:
        return x // 4 + 2


n = int(input())
a = 0
count = 0
for i in range(0, n):
    a = int(input())
    count += func(a)
print(count)