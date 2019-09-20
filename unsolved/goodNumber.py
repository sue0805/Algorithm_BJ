from collections import defaultdict as dd
import sys
input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().split()))
sums = [dd(int) for _ in range(n)]
result = 0

for i in range(n):
    if i != 0:
        sums[i].update(sums[i-1])
    found = False
    for j in range(0, i+1):
        sums[i][arr[i] + arr[j]] = 1
        if i != j:
            if sums[i - 1][arr[i] - arr[j]] == 1 and not found:
                result += 1
                found = True

# print(minuses)
print(result)