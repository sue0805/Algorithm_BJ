import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
area = [[0]*(n) for i in range(m)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(k):
    y, x, ey, ex = map(int, input().split())
    for i in range(x, ex):
        for j in range(y, ey):
            area[i][j] = 1

cnt = 0
size = []
visited = [[False] * (n) for i in range(m)]
for i in range(m):
    for j in range(n):
        if area[i][j] == 0 and not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = True
            cnt += 1
            tmp = 0
            while q:
                x, y = q.popleft()
                tmp += 1
                for d in dirs:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and area[nx][ny] == 0:
                        q.append((nx, ny))
                        visited[nx][ny] = True
            size.append(tmp)
print(cnt)
size.sort()
for s in size:
    print(s, end=" ")