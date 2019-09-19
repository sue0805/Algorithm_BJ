from itertools import combinations
from collections import deque
import sys
input = sys.stdin.readline
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n, m = map(int, input().split())
maps = [[0] * m for i in range(n)]
spaces = []
safe_area = 0
result = -1
for i in range(n):
    line = list(map(int, input().split()))
    for j, l in enumerate(line):
        if l != 0:
            maps[i][j] = l
        else:
            spaces.append((i, j))
            safe_area += 1


def bfs(x, y, walls, visited):
    q = deque()
    q.append((x, y))
    ret = 0
    while q:
        i, j = q.popleft()
        if maps[i][j] == 0:
            ret += 1
        for d in dirs:
            nx, ny = i + d[0], j + d[1]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if maps[nx][ny] == 0 and (nx, ny) not in walls:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return ret


combs = combinations(spaces, 3)
while True:
    try:
        walls = next(combs)
        visited = [[False] * m for i in range(n)]
        sa = safe_area - 3
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 2 and not visited[i][j]:
                    visited[i][j] = True
                    sa -= bfs(i, j, walls, visited)
        result = max(sa, result)
    except StopIteration:
        break

print(result)