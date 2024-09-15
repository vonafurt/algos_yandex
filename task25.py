n1 = input()
str1 = input().split()
n2 = input()
str2 = input().split()
n3 = input()
str3 = input().split()

nums = {}
buf2 = []
buf3 = []

for i in str1:
    nums[int(i)] = 1
for i in str2:
    if int(i) in nums and not int(i) in buf2:
        nums[int(i)] = 2
    else:
        nums[int(i)] = 1
        buf2.append(int(i))

for i in str3:
    if int(i) in nums and not int(i) in buf3:
        nums[int(i)] = 2
    else:
        nums[int(i)] = 1
        buf3.append(int(i))

keys_with_value_two = [key for key, value in nums.items() if value == 2]
keys_with_value_two = sorted(keys_with_value_two)

for i in keys_with_value_two:
    print(i, end=' ')