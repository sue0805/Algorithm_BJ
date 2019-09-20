import sys
from collections import deque
input = sys.stdin.readline

alphaNum = {}
for i, a in enumerate('ABCDEF'):
    alphaNum[a] = i

dirs = [(-2, 1), (-2, -1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

prev = [-1, -1]
start = [-1, -1]
visited = [[False] * 6 for i in range(6)]
for i in range(36):
    if -1 in prev:
        p = list(input())
        prev[0] = start[0] = int(p[1]) - 1
        prev[1] = start[1] = alphaNum[p[0].upper()]
        visited[prev[0]][prev[1]] = True
        continue
    else:
        p = list(input())
        p[0] = alphaNum[p[0].upper()]
        p[1] = int(p[1]) - 1
        valid = False
        for d in dirs:
            px, py = prev[0] + d[0], prev[1] + d[1]
            if px == p[1] and py == p[0] and not visited[px][py]:
                prev = [p[1], p[0]]
                valid = True
                visited[px][py] = True
                break
        if not valid:
            break

if valid:
    for v in visited:
        if False in v:
            valid = False
            break
    if valid:
        tour = False
        for d in dirs:
            px, py = prev[0] + d[0], prev[1] + d[1]
            if px == start[0] and py == start[1]:
                tour = True
                break
        if not tour:
            valid = False

print('Valid' if valid else 'Invalid')