count = 0

def slon(p, x, y):
    global count
    x1 = x - 1
    y1 = y - 1
    while 0 <= x1 < 8 and 0 <= y1 < 8: # left up
        if p[y1][x1] == 'R' or p[y1][x1] == 'B':
            break
        elif p[y1][x1] == '*':
            p[y1][x1] = 'X'
            count += 1
        x1 -= 1
        y1 -= 1
    x1 = x + 1
    y1 = y - 1
    while 0 <= x1 < 8 and 0 <= y1 < 8: # right up
        if p[y1][x1] == 'R' or p[y1][x1] == 'B':
            break
        elif p[y1][x1] == '*':
            p[y1][x1] = 'X'
            count += 1
        x1 += 1
        y1 -= 1
    x1 = x - 1
    y1 = y + 1
    while 0 <= x1 < 8 and 0 <= y1 < 8: #left down
        if p[y1][x1] == 'R' or p[y1][x1] == 'B':
            break
        elif p[y1][x1] == '*':
            p[y1][x1] = 'X'
            count += 1
        x1 -= 1
        y1 += 1
    x1 = x + 1
    y1 = y + 1
    while 0 <= x1 < 8 and 0 <= y1 < 8: # right down
        if p[y1][x1] == 'R' or p[y1][x1] == 'B':
            break
        elif p[y1][x1] == '*':
            p[y1][x1] = 'X'
            count += 1
        x1 += 1
        y1 += 1



def lad(p, x, y):
    global count
    for i in range(x - 1, -1, -1):
        if p[y][i] == 'R' or p[y][i] == 'B':
            break
        else:
            if p[y][i] == '*':
                p[y][i] = 'X'
                count += 1
    for i in range(x + 1, 8):
        if p[y][i] == 'R' or p[y][i] == 'B':
            break
        else:
            if p[y][i] == '*':
                p[y][i] = 'X'
                count += 1
    for i in range(y - 1, -1, -1):
        if p[i][x] == 'R' or p[i][x] == 'B':
            break
        else:
            if p[i][x] == '*':
                p[i][x] = 'X'
                count += 1
    for i in range(y + 1, 8):
        if p[i][x] == 'R' or p[i][x] == 'B':
            break
        else:
            if p[i][x] == '*':
                p[i][x] = 'X'
                count += 1


def swap(a):
    global count
    b = a.copy()
    for i in range(0, 8):
        for j in range(0, 8):
            if a[i][j] == 'R':
                lad(b, j, i)
                count += 1
            if a[i][j] == 'B':
                slon(b, j, i)
                count += 1
    return(b)


a = []
for i in range(0, 8):
    x = [char for char in input() if char != ' ']
    a.append(x)

swap(a)

#for element in swap(a):
#    print(element)
print(64 - count)