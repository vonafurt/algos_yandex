def func():
    max_value = i
    value_index_right = nums.index(max_value)
    value_index_left = nums.index(max_value) - n

    force_right = value_index_right * k
    force_left = abs(value_index_left) * k

    #if force_left < b and a - force_left <= k or force_right < b and a - force_right <= k:
    if force_left < b or force_right < b:
        while force_left < b:
            if a - force_left <= k:
                return (max_value)
            force_left += n * k
        while force_right < b:
            if a - force_right <= k:
                return (max_value)
            force_right += n * k
    return -1

n = int(input())
nums = list(map(int, input().split()))
a, b, k = map(int, input().split())

while a - n * k > 0:
    a -= n * k
    b -= n * k

max_to_min = sorted(nums, reverse=True)

ans = 0

for i in max_to_min:
    ans = func()
    if ans != -1:
        break
if ans == -1:
    ans = nums[0]
print(ans)