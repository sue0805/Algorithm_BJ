N = int(input())
tmp = N // 2 + 1 if N % 2 != 0 else N // 2
colors = [1, 2, 3]
c = 0
for _ in range(0, int(input())):
    a, b = map(int, input().split())
    b -= 1
    a -= 1
    b = N - 1 - b if b >= tmp else b
    a = N - 1 - a if a >= tmp else a
    print(colors[b % 3] if a >= b else colors[a % 3])
