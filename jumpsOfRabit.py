import sys

direction = {"U": [-1, 0], "D": [1, 0], "L": [0, -1], "R": [0, 1]}
N, K = map(int, sys.stdin.readline().split())
arr = [0] * (2*N - 1)
tmp = 0
j = 0
for i in range(2*N - 1):
    if i < N:
        arr[i] = i+1 + tmp
        j = i+1
    else:
        j -= 1
        arr[i] = j + tmp
    tmp = arr[i]

jumps = sys.stdin.readline().splitlines()[0]
now = [0, 0]
sum = 1
for jump in jumps:
    d = direction[jump]
    num = 0
    now[0] += d[0]
    now[1] += d[1]

    if now[0] + now[1] > 0:
        num += arr[(now[0] + now[1]) - 1]

    if (now[0] + now[1]) % 2 == 0:
        if now[0] + now[1] < N:
            num += now[1] + 1
        else:
            num += N - now[0]
    else:
        if now[0] + now[1] < N:
            num += now[0] + 1
        else:
            num += N - now[1]
    sum += num

print(sum)