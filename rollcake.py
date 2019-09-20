l = int(input())
n = int(input())

cakes = [0] * (l+1)
max_p = -1
max_c = -1
expected = -1
real = -1

for i in range(1, n+1):
    fr, to = map(int, input().split())
    cnt = 0
    if max_p < to - fr:
        max_p = to - fr
        expected = i
    for j in range(fr, to+1):
        if cakes[j] == 0:
            cakes[j] = i
            cnt += 1
    if cnt > max_c:
        max_c = cnt
        real = i

print(expected)
print(real)