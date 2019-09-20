from collections import deque

n, k = map(int, input().split())

moves = [-1, 1, 2]
visited = [False] * 200001

q = deque()
q.append((n, 0))

while q:
    curr, t = q.popleft()
    if curr == k:
        print(t)
        break
    for move in moves:
        if move == 2 and 2*curr <= 200000 and not visited[2*curr]:
            q.append((2*curr, t+1))
            visited[2*curr] = True
        elif abs(move) == 1 and 0 <= curr+move <= 200000:
            if not visited[curr + move]:
                q.append((curr + move, t+1))
                visited[curr+move] = True