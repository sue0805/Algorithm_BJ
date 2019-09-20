import queue
from collections import defaultdict

n, m, a, b, k = map(int, input().split())
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = defaultdict(bool)

for i in range(k):
    x, y = map(int, input().split())
    visited[(x-1, y-1)] = True

x, y = map(int, input().split())
x -= 1
y -= 1
start = []
for i in range(a):
    for j in range(b):
        start.append((x+i, y+j))

x, y = map(int, input().split())
goal = []
x -= 1
y -= 1
for i in range(a):
    for j in range(b):
        goal.append((x+i, y+j))

q = queue.Queue()
q.put((start, 0))
visited[tuple(start)] = True
result = -1

while not q.empty():
    now, cnt = q.get()
    if now[0] == goal[0]:
        result = cnt
        break
    for d in dirs:
        tmp = []
        for x, y in now:
            i, j = x + d[0], y + d[1]
            if 0 <= i < n and 0 <= j < m and not visited[(i, j)]:
                tmp.append((i, j))
            else:
                break
        if len(tmp) == len(start) and not visited[tuple(tmp)]:
            q.put((tmp, cnt + 1))
            visited[tuple(tmp)] = True

print(result)