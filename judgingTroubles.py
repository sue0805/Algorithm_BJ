import sys

n = int(sys.stdin.readline())
doms = {}
for i in range(n):
    dom = sys.stdin.readline()
    doms[dom] = doms[dom] + 1 if dom in doms else 1
cnt = 0
for i in range(n):
    kattis = sys.stdin.readline()
    if kattis in doms and doms[kattis] > 0:
        doms[kattis] -= 1
        cnt += 1

print(cnt)