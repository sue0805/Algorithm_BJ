import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
lands = [list() for i in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
lowest = 101
highest = 0
for i in range(n):
    line = list(map(int, input().split()))
    lands[i] = line
    lowest = min(min(line), lowest)
    highest = max(max(line), highest)

lowest -= 1
result = -1

for rain in range(lowest, highest):
    visited = [[False] * n for i in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if lands[i][j] > rain and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                cnt += 1
                while q:
                    x, y = q.popleft()
                    for d in dirs:
                        nx, ny = x + d[0], y + d[1]
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                            if lands[nx][ny] > rain:
                                visited[nx][ny] = True
                                q.append((nx, ny))
    result = max(cnt, result)

print(result)