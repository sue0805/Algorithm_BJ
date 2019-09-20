from collections import deque

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(i, j, land, visited):
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.pop()
        visited[x][y] = True
        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < len(land) and 0 <= ny < len(land[0]) and land[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    land = [[0] * m for i in range(n)]
    visited = [[False] * m for i in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        land[y][x] = 1
    cnt = 0

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                bfs(i, j, land, visited)
                cnt += 1
    print(cnt)