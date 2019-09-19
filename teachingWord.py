from itertools import combinations
import sys

n, k = map(int, sys.stdin.readline().split())
default = set(list('antatica'))
chars = set()
cnt = len(default)

if cnt > k:
    print(0)
    exit(0)

arr = []
result = 0

for i in range(n):
    word = list(sys.stdin.readline())
    tmp = set(word[4:len(word)-4]) - default
    if len(tmp) + cnt <= k:
        arr.append(tmp)
        chars.update(tmp)
        result = 1

n = len(arr)
if result == 0:
    print(0)
    exit(0)

if len(chars) <= k - cnt:
    result = len(arr)
else:
    tmp = list(combinations(chars, k - cnt))
    for t in tmp:
        t = set(list(t))
        c = 0
        for a in arr:
            if not (a - t):
                c += 1
        result = max(result, c)


print(result)