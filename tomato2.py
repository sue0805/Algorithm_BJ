import sys
from collections import deque
input = sys.stdin.readline

m, n, h = map(int, input().split())
boxes = [[[0] * m for i in range(n)] for i in range(h)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
floors = [-1, 1]
tomatoes = deque()

for i in range(h):
    for j in range(n):
        row = list(map(int, input().split()))
        for k in range(m):
            boxes[i][j][k] = row[k]
            if boxes[i][j][k] == 1:
                tomatoes.append((i, j, k))


def bfs(q, t):
    changed = False
    while q:
        i, j, k = q.popleft()
        for d in dirs:
            x, y, z = i, j + d[0], k + d[1]
            if 0 <= y < n and 0 <= z < m and boxes[x][y][z] == 0:
                boxes[x][y][z] = 1
                t.append((x, y, z))
                changed = True
        for f in floors:
            x, y, z = i + f, j, k
            if 0 <= x < h and boxes[x][y][z] == 0:
                boxes[x][y][z] = 1
                t.append((x, y, z))
                changed = True
    return changed


cnt = 0
while True:
    q = deque()
    while tomatoes:
        q.append(tomatoes.popleft())
    changed = bfs(q, tomatoes)
    if not changed:
        for i in range(h):
            for j in range(n):
                if boxes[i][j].count(0) > 0:
                    print(-1)
                    exit(0)
        break
    cnt += 1

print(cnt)