board = []
for i in range(10):
    board.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

n = int(input())
positions = []
for i in range(n):
    positions.append(list(map(int, input().split())))
for pos in positions:
    board[pos[0]][pos[1]] = 1