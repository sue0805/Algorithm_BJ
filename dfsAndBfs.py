from collections import deque

n, m, v = map(int, input().split())
visited = [False] * (n+1)
adj = [list() for i in range(n+1)]

for i in range(m):
    fr, to = map(int, input().split())
    adj[fr].append(to)
    adj[to].append(fr)

for a in adj:
    a.sort()


def dfs(v):
    visited[v] = True
    print(v, end=" ")
    for to in adj[v]:
        if not visited[to]:
            dfs(to)


def bfs(v):
    q = deque()
    q.append(v)
    while q:
        p = q.popleft()
        if visited[p]:
            continue
        visited[p] = True
        print(p, end=" ")
        for to in adj[p]:
            if not visited[to]:
                q.append(to)


dfs(v)
visited = [False] * (n+1)
print()
bfs(v)