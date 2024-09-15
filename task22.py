def func(w1, w2):
    flag = 0
    for key1, value1 in w1.items():
        for key2, value2 in w2.items():
            if key1 == key2:
                flag = 1
                if value1 != value2:
                    return -1
        if flag == 0:
            return -1
        flag = 0
    return 1




str1 = input()
str2 = input()


word1 = {}
word2 = {}


for i in str1:
    if i in word1:
        word1[i] += 1
    else:
        word1[i] = 1
for i in str2:
    if i in word2:
        word2[i] += 1
    else:
        word2[i] = 1

if func(word1, word2) == 1:
    print("YES")
else:
    print("NO")