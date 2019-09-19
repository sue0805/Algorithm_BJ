import sys

cost = list(map(int, input().split()))
area = [[0] * 101 for i in range(3)]
min_fr = sys.maxsize
max_to = -sys.maxsize

for i in range(3):
    fr, to = map(int, input().split())
    min_fr, max_to = min(min_fr, fr), max(max_to, to)
    for j in range(fr, to):
        area[i][j] = 1

result = 0
for j in range(min_fr, max_to):
    cnt = 0
    for i in range(3):
        if area[i][j] == 1:
            cnt += 1
    result += cost[cnt-1] * cnt

print(result)