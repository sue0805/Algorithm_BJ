N = int(input())
land = [[0] * (N + 1) for i in range(N + 1)]
fx = [-1, 1, -1, 1]
fy = [1, 1, -1, -1]
dx = [0, 1, 0, 1]
dy = [0, 0, -1, -1]


def getRevenue(y, x, dir):
    revLand = [[0] * (N + 1) for i in range(N + 1)]
    revenue = list()
    for i in range(y, N + 1 if fy[dir] > 0 else 0, fy[dir]):
        horSum = 0
        for j in range(x, N + 1 if fx[dir] > 0 else 0, fx[dir]):
            horSum += land[i][j]
            revLand[i][j] = revLand[i - fy[dir]][j] + horSum
            revenue.append(revLand[i][j])
    return revenue


def pointCount(y, x):
    same = 0
    for dir in range(2):
        left = getRevenue(y + dy[dir], x + dx[dir], dir)
        rd = 3 - dir
        right = getRevenue(y + dy[rd], x + dx[rd], rd)

        for l in left:
            for r in right:
                if l == r:
                    same += 1
    return same


for i in range(1, N + 1):
    land[i] = [0] + list(map(int, input().split()))

allCount = 0
for i in range(2, N + 1):
    for j in range(1, N):
        allCount += pointCount(i, j)

print(allCount)