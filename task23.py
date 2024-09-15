n = int(input())

str1 = input().split()

word1 = {}

for i in str1:
    if int(i) in word1:
        word1[int(i)] += 1
    else:
        word1[int(i)] = 1


max_value = 0
max_nums = 0

for keys in word1:
    if word1[keys] > max_nums:
        max_nums = word1[keys]
    if keys + 1 in word1:
        if word1[keys] + word1[keys + 1] > max_value:
            max_value = word1[keys] + word1[keys + 1]
if max_value != 0:
    print(n - max_value)
else:
    print(n - max_nums)