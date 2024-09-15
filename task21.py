import time
n = int(input())
t = time.time()
music = {}

for i in range(n):
    k = int(input())
    words = input().split()
    for word in words:
        if word in music:
            music[word] += 1
        else:
            music[word] = 1

words = []
count = 0

for key, value in music.items():
    if value == n:
        words.append(key)
        count += 1

print(count)
words = sorted(words)
for i in words:
    print(i, ' ', end='')
