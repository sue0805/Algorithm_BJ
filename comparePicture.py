from itertools import combinations

n = int(input())
images = [[list() for _ in range(5)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(5):
        images[i][j] = list(input())


def compare(a, b):
    cnt = 0
    for i in range(5):
        for j in range(7):
            if images[a][i][j] != images[b][i][j]:
                cnt += 1
    return cnt


combs = list(combinations(range(1, n+1), 2))
result = ()
diff = 36
for c in combs:
    tmp = compare(c[0], c[1])
    if tmp < diff:
        diff = tmp
        result = (str(c[0]), str(c[1]))

print(' '.join(result))