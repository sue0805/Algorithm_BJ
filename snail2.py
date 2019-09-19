import sys
sys.setrecursionlimit(10**6)

m, n = map(int, input().split())
visited = [[False] * n for i in range(m)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(i, j, cnt, direction):
    visited[i][j] = True
    x = i + dirs[direction][0]
    y = j + dirs[direction][1]
    if 0 <= x < m and 0 <= y < n and not visited[x][y]:
        dfs(x, y, cnt, direction)
    else:
        direction = direction + 1 if direction + 1 <= 3 else 0
        x = i + dirs[direction][0]
        y = j + dirs[direction][1]
        if 0 <= x < m and 0 <= y < n and not visited[x][y]:
            dfs(x, y, cnt + 1, direction)
        else:
            print(cnt)


dfs(0, 0, 0, 0)