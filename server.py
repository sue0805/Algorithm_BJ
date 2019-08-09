n, T = map(int, input().split())
works = list(map(int, input().split()))

cnt = 0
for work in works:
    if T - work >= 0:
        cnt += 1
        T -= work
    else:
        break

print(cnt)
