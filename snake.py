import sys

n = int(sys.stdin.readline())
board = [[-1] * n for i in range(n)]
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
k = int(sys.stdin.readline())
for i in range(k):
    y, x = map(int, sys.stdin.readline().split())
    board[y-1][x-1] = 1

l = int(sys.stdin.readline())
t = [tuple(sys.stdin.readline().split()) for i in range(l)]
i = 1
snake = [[0, 0]]
dir = 0
while True:
    snake.append([snake[-1][0] + d[dir][0], snake[-1][1] + d[dir][1]])
    if not(0 <= snake[-1][0] < n) or not(0 <= snake[-1][1] < n) or board[snake[-1][0]][snake[-1][1]] == 0:
        break
    elif board[snake[-1][0]][snake[-1][1]] == -1:
        y, x = snake.pop(0)
        board[y][x] = -1
    board[snake[-1][0]][snake[-1][1]] = 0
    if len(t) > 0:
        time = int(t[0][0])
        rotate = t[0][1]
        if time == i:
            t.pop(0)
            if rotate == 'L':
                dir = dir - 1 if dir - 1 >= 0 else 3
            else:
                dir = dir + 1 if dir + 1 < 4 else 0
    i += 1
print(i)