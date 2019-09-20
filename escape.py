import sys

r, c = map(int, sys.stdin.readline().split())
forest = []
dochis = [[-1, -1]]
water =[]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for i in range(r):
    line = list(sys.stdin.readline())
    forest.append(line)
    if line.count('S') > 0:
        dochis = [[i, line.index('S')]]
    for j in range(c):
        if line[j] == '*':
            water.append([i, j])


def flooding():
    global water
    new_water = []
    while len(water) > 0:
        x, y = water.pop()
        for i in range(4):
            a, b = x + d[i][0], y + d[i][1]
            if 0 <= a < r and 0 <= b < c and forest[a][b] == '.':
                forest[a][b] = '*'
                new_water.append([a, b])
    water = new_water


move = 0
while True:
    if len(dochis) == 0:
        print('KAKTUS')
        exit(0)
    flooding()

    move += 1

    new_dochis = []
    for dochi in dochis:
        for i in range(4):
            x, y = dochi[0] + d[i][0], dochi[1] + d[i][1]
            if 0 <= x < r and 0 <= y < c:
                if forest[x][y] == '.':
                    forest[x][y] = 'S'
                    new_dochis.append([x, y])
                elif forest[x][y] == 'D':
                    print(move)
                    exit(0)
    dochis = new_dochis
