from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for i in range(n)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 0
visited = [[False] * m for i in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1 and not visited[i][j]:
            q.append((i, j))
            visited[i][j] = True
while True:
    changed = False
    newq = deque()
    while q:
        x, y = q.popleft()
        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0 and not visited[nx][ny]:
                changed = True
                newq.append((nx, ny))
                box[nx][ny] = 1
                visited[nx][ny] = True
    if not changed:
        for b in box:
            for tomato in b:
                if tomato == 0:
                    print(-1)
                    exit(0)
        break
    cnt += 1
    q = newq

print(cnt)
