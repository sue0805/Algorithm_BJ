from collections import deque, defaultdict

n, m, l = map(int, input().split())

players = deque([i for i in range(1, n+1)])
cnt = defaultdict(int)
result = 0
d = 1

while True:
    player = players[0]
    cnt[player] += 1
    if cnt[player] == m:
        break
    if cnt[player] % 2 == 0:
        d = 1
    else:
        d = -1
    for i in range(l):
        players.rotate(d)
    result += 1

print(result)
