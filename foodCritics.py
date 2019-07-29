N, M = map(int, input().split())

pieces = [[1] * M for i in range(0, N)]

cnt = 0
knife = 0
sausage = N * M
for p in pieces:
    for i in range(0, sausage):
        cnt += 1
        p.remove(1)
        sausage -= 1
        if cnt % N == 0 and len(p) != 0:
            knife += 1
        if len(p) == 0:
            break
print(knife)

