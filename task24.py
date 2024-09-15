n, k = map(int, input().split())
str1 = input().split()

word1 = {}

for idx, val in enumerate(str1):
    if int(val) in word1 and idx - word1[int(val)] <= k:
        print("YES")
        break
    word1[int(val)] = idx
else:
    print("NO")