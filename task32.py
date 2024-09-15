import time

def func(n):
    left = 0
    left_buff = left
    right = 100000000
    right_buff = right
    k = 0
    while left < right:
        mid = (left + right) // 2
        for i in range(mid, 0, -1):
            k += i * (mid - i + 1) + (mid - i + 1)
            if k >= n:
                break
        if k >= n:
            right = mid + 1
        else:
            left = mid - 1
        if left_buff == left and right_buff == right:
            return mid
        left_buff = left
        right_buff = right
        k = 0
        #mid = (left + right) // 2
        #print(left, ' ', mid, ' ', right)
    return mid + 1

n = int(input()) + 2
t = time.time()
if n > 2:
    res = func(n)
else:
    res = 0
print(res)




