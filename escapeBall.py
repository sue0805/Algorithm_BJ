import queue

n, m = map(int, input().split())
board = [list(input().strip()) for i in range(n)]
visited = [[[[False] * m for i in range(n)] for i in range(m)] for i in range(n)]
dirs = [(1, 0, 'D'), (-1, 0, 'U'), (0, 1, 'R'), (0, -1, 'L')]
q = queue.Queue()
result = -1

rx = ry = bx = by = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
q.put((rx, ry, bx, by, 0))
visited[rx][ry][bx][by] = True

def move(x, y, dx, dy, c):
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        c += 1
    return x, y, c

while not q.empty():
    rx, ry, bx, by, cnt = q.get()
    for d in dirs:
        rx_, ry_, rc = move(rx, ry, d[0], d[1], 0)
        bx_, by_, bc = move(bx, by, d[0], d[1], 0)
        if board[bx_][by_] == 'O':
            continue
        if board[rx_][ry_] == 'O':
            result = cnt + 1
            break
        if rx_ == bx_ and ry_ == by_:
            if rc > bc:
                rx_, ry_ = rx_ - d[0], ry_ - d[1]
            else:
                bx_, by_ = bx_ - d[0], by_ - d[1]
        if not visited[rx_][ry_][bx_][by_]:
            visited[rx_][ry_][bx_][by_] = True
            q.put((rx_, ry_, bx_, by_, cnt + 1))
    if result != -1:
        break
print(result)