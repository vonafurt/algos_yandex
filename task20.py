from copy import deepcopy

def one_rectangle(grid, count):
    x, y, x_len, y_len = 0, 0, 0, 0
    x_buf, y_buf = 0, 0
    found = False
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'a':
                x = i
                y = j
                x_buf = x
                y_buf = y
                while x < rows and grid[x][y_buf] == 'a':
                    x += 1
                while y < cols and grid[x_buf][y] == 'a':
                    y += 1
                x_len = x - i
                y_len = y - j
                found = True
                break
        if found:
            break
    if x_len == 1 or y_len == 1:
        grid[x_buf][y_buf] = 'b'
    else:
        for i in range(x_buf, x):
            grid[i][y_buf] = 'b'

def draw(grid):
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            print(grid[i][j], end='')
        print()

def check_rect_cols(grid, x1, y1, x2, y2):
    for h in range(x1, x2):
        for f in range(y1, y2):
            if grid[h][f] != "#":
                return f - 1
    return "True"

def check_rect_cols1(grid, x1, y1, x2, y2):
    for h in range(x1, x2):
        for f in range(y1, y2):
            if grid[h][f] != "#":
                return h - 1
    return "True"


def count_rectangles(grid, grid1):

    letter_count = 0
    count = 0
    count1 = 0
    letter_count1 = 0
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    flag = False
    rectangles = 0
    rectangles1 = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                rectangles += 1
                if rectangles > 2:
                    flag = True
                    rectangles = 10
                    break
                k = i
                l = j
                while grid[k][j] == "#":
                    k += 1
                while grid[i][l] == "#":
                    l += 1
                while check_rect_cols(grid, i, j, k, l) != "True":
                    l = check_rect_cols(grid, i, j, k, l)
                if letter_count == 0:
                    if j != l and i != k:
                        for m in range(i, k):
                            for n in range(j, l):
                                grid[m][n] = 'a'
                                count += 1
                    if j != l and i == k:
                        for n in range(j, l):
                            grid[k][n] = 'a'
                            count += 1
                    if j == l and i != k:
                        for m in range(i, k):
                            grid[m][l] = 'a'
                            count += 1
                    if j == l and i == k:
                        grid[i][j] = 'a'
                        count += 1
                elif letter_count == 1:
                    if j != l and i != k:
                        for m in range(i, k):
                            for n in range(j, l):
                                grid[m][n] = 'b'
                                count += 1
                    if j != l and i == k:
                        for n in range(j, l):
                            grid[k][n] = 'b'
                            count += 1
                    if j == l and i != k:
                        for m in range(i, k):
                            grid[m][l] = 'b'
                            count += 1
                    if j == l and i == k:
                        grid[i][j] = 'b'
                        count += 1
                else:
                    if j != l and i != k:
                        for m in range(i, k):
                            for n in range(j, l):
                                grid[m][n] = '.'
                                count += 1
                    if j != l and i == k:
                        for n in range(j, l):
                            grid[k][n] = '.'
                            count += 1
                    if j == l and i != k:
                        for m in range(i, k):
                            grid[m][l] = '.'
                            count += 1
                    if j == l and i == k:
                        grid[i][j] = '.'
                        count += 1
                letter_count += 1
        if flag == True:
            break

    flag = False

    for j in range(cols):
        for i in range(rows):
            if grid1[i][j] == '#':
                rectangles1 += 1
                if rectangles1 > 2:
                    flag = True
                    rectangles1 = 10
                    break
                k = i
                l = j
                while grid1[k][j] == "#":
                    k += 1
                while grid1[i][l] == "#":
                    l += 1
                while check_rect_cols1(grid1, i, j, k, l) != "True":
                    l = check_rect_cols1(grid1, i, j, k, l)
                if letter_count1 == 0:
                    if j != l and i != k:
                        for m in range(i, k):
                            for n in range(j, l):
                                grid1[m][n] = 'a'
                                count1 += 1
                    if j != l and i == k:
                        for n in range(j, l):
                            grid1[k][n] = 'a'
                            count1 += 1
                    if j == l and i != k:
                        for m in range(i, k):
                            grid1[m][l] = 'a'
                            count1 += 1
                    if j == l and i == k:
                        grid1[i][j] = 'a'
                        count1 += 1
                elif letter_count1 == 1:
                    if j != l and i != k:
                        for m in range(i, k):
                            for n in range(j, l):
                                grid1[m][n] = 'b'
                                count1 += 1
                    if j != l and i == k:
                        for n in range(j, l):
                            grid1[k][n] = 'b'
                            count1 += 1
                    if j == l and i != k:
                        for m in range(i, k):
                            grid1[m][l] = 'b'
                            count1 += 1
                    if j == l and i == k:
                        grid1[i][j] = 'b'
                        count1 += 1
                else:
                    if j != l and i != k:
                        for m in range(i, k):
                            for n in range(j, l):
                                grid1[m][n] = '.'
                                count1 += 1
                    if j != l and i == k:
                        for n in range(j, l):
                            grid1[k][n] = '.'
                            count1 += 1
                    if j == l and i != k:
                        for m in range(i, k):
                            grid1[m][l] = '.'
                            count1 += 1
                    if j == l and i == k:
                        grid1[i][j] = '.'
                        count1 += 1
                letter_count1 += 1
        if flag:
            break

    return rectangles, count, rectangles1, count1


m, n = map(int, input().split())
holst = []
holst.append(['.'] * (n + 2))
for i in range(m):
    x = [char for char in input() if char != ' ']
    x = ['.'] + x + ['.']
    holst.append(x)
holst.append(['.'] * (n + 2))
holst1 = deepcopy(holst)

cnt = count_rectangles(holst, holst1)

if cnt[0] <= cnt[2]:
    if cnt[0] > 2 or cnt[1] < 2:
        print("NO")
    elif cnt[0] == 2:
        print("YES")
        draw(holst)
    elif cnt[0] == 1:
        print("YES")
        one_rectangle(holst, cnt[1])
        draw(holst)
else:
    if cnt[2] > 2 or cnt[3] < 2:
        print("NO")
    elif cnt[2] == 2:
        print("YES")
        draw(holst1)
    elif cnt[2] == 1:
        print("YES")
        one_rectangle(holst1, cnt[3])
        draw(holst1)
