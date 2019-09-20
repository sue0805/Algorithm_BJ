import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
image = [list(input().rstrip()) for i in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

cb = 0
nb = 0


def dfs(x, y, t, visited):
    color = image[x][y]
    if t == 'cb' and color in 'RG':
        color = 'RG'

    for d in dirs:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if image[nx][ny] in color:
                visited[nx][ny] = True
                dfs(nx, ny, t, visited)

t = 'cb'
for _ in range(2):
    visited = [[False] * n for i in range(n)]
    if _ == 1:
        t = 'nb'
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                if t == 'nb':
                    nb += 1
                else:
                    cb += 1
                dfs(i, j, t, visited)

print(nb, cb)