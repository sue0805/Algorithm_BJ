from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
adj = [list() for i in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

result = 0
visited = [False] * (n+1)
q = deque()
for i in range(1, n+1):
    if not visited[i]:
        q.append(i)
        result += 1
        while q:
            now = q.popleft()
            for j in adj[now]:
                if not visited[j]:
                    q.append(j)
                    visited[j] = True

print(result)