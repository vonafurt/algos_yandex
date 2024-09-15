board = []
board.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
for i in range(8):
    board.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
board.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    board[x][y] = 1

length = 0

for i in range(1, 9):
    for j in range(1, 9):
        count = 0
        if board[i][j] == 1:
            if board[i - 1][j] == 0:
                count += 1
            if board[i][j - 1] == 0:
                count += 1
            if board[i + 1][j] == 0:
                count += 1
            if board[i][j + 1] == 0:
                count += 1
        length += count

print(length)
