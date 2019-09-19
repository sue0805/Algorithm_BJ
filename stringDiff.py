import sys

a, b = input().split()

dif = len(b) - len(a)
min_d = sys.maxsize
result = 0

for i in range(dif+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[j + i]:
            cnt += 1
    if min_d > cnt:
        min_d = cnt


print(min_d)
