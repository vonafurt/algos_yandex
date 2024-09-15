def draw(a1, b1, a2, b2):
    if a1 + a2 < b1 + b2:
        return b1 + b2 - (a1 + a2)
    else:
        return 0


def func1(a1, b1, a2, b2):
    if a1 + a2 == b1 + b2:
        if b1 >= a2:
            return 1
        elif a2 > b1:
            return 0
        else:
            return 0
    else:
        return 0


def func2(a1, b1, a2, b2):
    if a1 + a2 == b1 + b2:
        if b2 >= a1:
            return 1
        elif a1 > b2:
            return 0
        else:
            return 0
    else:
        return 0

a1, b1 = map(int, input().split(':'))
a2, b2 = map(int, input().split(':'))
home = int(input())
#home = 2

count = draw(a1, b1, a2, b2)
a2 += draw(a1, b1, a2, b2)
if home == 1:
    count += func1(a1, b1, a2, b2)
else:
    count += func2(a1, b1, a2, b2)

print(count)