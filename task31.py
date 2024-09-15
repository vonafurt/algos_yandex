import time


def binary_search_right(arr, x):
    global n
    left, right = 0, n - 1
    result_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            result_index = mid
            left = mid + 1
        else:
            right = mid - 1

    return result_index


def binary_search_left(arr, x):
    global n
    left, right = 0, n - 1
    result_index = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= x:
            result_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return result_index


with open('input.txt', 'r') as file:
    lines = file.readlines()

n = int(lines[0])
t = time.time()
arr = list(map(int, lines[1].split()))
arr = sorted(arr)
arr_min = arr[0]
arr_max = arr[-1]
arr_min_ind = 0
arr_max_ind = n - 1
arr_len = n

k = int(lines[2])
for i in range(k):
    b, c = map(int, lines[i + 3].split())
    if b < arr_min and c < arr_min:
        print(0, end=' ')
    elif b > arr_max and c > arr_max:
        print(0, end=' ')
    elif b > arr_min and c < arr_max:
        x = binary_search_left(arr, b)
        y = binary_search_right(arr, c)
        print(y - x + 1, end=' ')
    elif b > arr_min and c >= arr_max:
        x = binary_search_left(arr, b)
        print(arr_max_ind - x + 1, end=' ')
    elif b <= arr_min and c < arr_max:
        y = binary_search_right(arr, c)
        print(y - arr_min_ind + 1, end=' ')
    elif b <= arr_min and c >= arr_max:
        print(n, end=' ')
#print(time.time() - t)
