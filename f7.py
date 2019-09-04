import sys

n = int(sys.stdin.readline())
drivers = [int(sys.stdin.readline()) for _ in range(n)]
maxScore = 0
drivers.sort(reverse=True)

cnt = 0
for i in range(n):
    if drivers[i] + n >= maxScore:
        cnt += 1
    maxScore = max(maxScore, drivers[i] + i + 1)
print(cnt)