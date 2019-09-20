import queue

n, m = map(int, input().split())

maze = [list(input()) for i in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = [[False] * m for i in range(n)]

q = queue.Queue()
q.put((0, 0, 1))
visited[0][0] = True
while not q.empty():
    x, y, cnt = q.get()
    if x == n-1 and y == m-1:
        print(cnt)
        break
    for d in dirs:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == '1' and not visited[nx][ny]:
            q.put((nx, ny, cnt+1))
            visited[nx][ny] = True