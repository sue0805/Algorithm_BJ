import queue

n = int(input())
apts = [list() for i in range(n)]
visited = [[False] * n for i in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for i in range(n):
    apts[i] = list(input())


def bfs(i, j):
    cnt = 0
    q = queue.Queue()
    q.put((i, j))
    visited[i][j] = True
    while not q.empty():
        x, y = q.get()
        for d in dirs:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < n and 0 <= ny < n and apts[nx][ny] == '1' and not visited[nx][ny]:
                q.put((nx, ny))
                cnt += 1
                visited[nx][ny] = True
        if q.empty():
            return cnt + 1



arr = []
for i in range(n):
    for j in range(n):
        if apts[i][j] == '1' and not visited[i][j]:
            cnt = bfs(i, j)
            arr.append(cnt)

print(len(arr))
arr.sort()
for a in arr:
    print(a)