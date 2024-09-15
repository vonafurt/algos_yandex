import time

word_set = set(input().split())
words = input().split()
t = time.time()
flag = 0
buf = ""
ind = 0

for word in words:
    for i in range(len(word)):
        buf = buf + word[i]
        if buf in word_set:
            words[ind] = buf
            break
        for j in word_set:
            if not j.startswith(buf):
                flag = 1
                break
        if flag == 1:
            flag = 0
            break

    buf = ""
    print(words[ind], end=' ')
    ind += 1

print(time.time() - t)
