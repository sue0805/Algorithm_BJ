from collections import deque, defaultdict

n = int(input())
adj = [list() for i in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(len(line)):
        if line[j] == 1:
            adj[i].append(j)

ways = []

for i in range(n):
    q = deque()
    q.append(i)
    tmp = []
    visited = defaultdict(bool)
    while q:
        now = q.popleft()
        tmp.append(now)
        for p in adj[now]:
            if not visited[p]:
                q.append(p)
                visited[p] = True
    ways.append(tmp)

for i in range(n):
    tmp = ['0'] * n
    for j, w in enumerate(ways[i]):
        if j != 0:
            tmp[w] = '1'
    print(' '.join(tmp))