import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
sea = [[0] * m for i in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
icebergs = deque()
for i in range(n):
    row = map(int, input().split())
    for j, r in enumerate(row):
        sea[i][j] = r
        if r > 0:
            icebergs.append((i, j))


def dfs(x, y, visited, rem):
    cnt = 0
    if sea[x][y] == 0:
        return

    for d in dirs:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < m:
            if sea[nx][ny] == 0:
                cnt += 1
            elif sea[nx][ny] > 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny, visited, rem)
    rem.append((x, y, cnt))


year = 0
while True:
    visited = [[False] * m for i in range(n)]
    cnt = 0
    rem = deque()
    for i, j in icebergs:
        if not visited[i][j]:
            visited[i][j] = True
            cnt += 1
            dfs(i, j, visited, rem)

    while rem:
        x, y, c = rem.popleft()
        sea[x][y] -= c
        if sea[x][y] <= 0:
            sea[x][y] = 0
            icebergs.remove((x, y))

    if cnt > 1:
        print(year)
        break
    if not icebergs:
        print(0)
        break
    year += 1