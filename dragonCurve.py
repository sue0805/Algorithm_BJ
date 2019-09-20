from collections import deque

n = int(input())
dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
board = [[0] * 101 for i in range(101)]


def make_curve(start, d, g, now, dq):
    tmp = deque()
    if now == 0:
        tmp.append(d)
        board[start[0]][start[1]] = 1
        start[0] += dirs[d][0]
        start[1] += dirs[d][1]
        board[start[0]][start[1]] = 1
    else:
        tmp = deque(dq)
        while dq:
            direction = dq.pop()
            direction = direction + 1 if direction + 1 <= 3 else 0
            tmp.append(direction)
            start[0] += dirs[direction][0]
            start[1] += dirs[direction][1]
            board[start[0]][start[1]] = 1
    if now == g:
        return
    make_curve(start, d, g, now + 1, tmp)


for i in range(n):
    x, y, d, g = map(int, input().split())
    make_curve([y, x], d, g, 0, deque())

result = 0

for i in range(100):
    for j in range(100):
        if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] == 1:
            result += 1

print(result)