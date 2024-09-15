import random

def custom_random():
    if random.random() < 0.25:
        return 1  # значение 1 с вероятностью 1/4
    else:
        return 0  # значение 0 с вероятностью 3/4

a = []
count = 0
m = 10000

for i in range(m):
    for j in range(17):
        a.append(custom_random())
    for j in range(16):
        if a[i] == 0 and a[i + 1] == 1:
            count += 1
print(count / m)