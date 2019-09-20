def solution():
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    n, k = map(int, input().split())
    maps = [list() for i in range(n)]
    max_h = 0
    max_l = [0]
    for i in range(n):
        maps[i] = list(map(int, input().split()))
        max_h = max(max(maps[i]), max_h)

    def dfs(i, j, value, p, l):
        for d in dirs:
            x, y = i + d[0], j + d[1]
            if 0 <= x < n and 0 <= y < n:
                if maps[x][y] < value and [x, y] not in l:
                    dfs(x, y, maps[x][y], p, l + [[x, y]])
                else:
                    if p != 0 and [x, y] not in l:
                        for depth in range(1, p+1):
                            tmp = maps[x][y] - depth
                            if tmp < 0 or tmp >= value:
                                continue
                            dfs(x, y, tmp, 0, l + [[x, y]])
        max_l[0] = max(max_l[0], len(l))

    for i in range(n):
        for j in range(n):
            if maps[i][j] == max_h:
                dfs(i, j, maps[i][j], k, [[i, j]])

    return max_l[0]


for i in range(1, int(input()) + 1):
    print('#{} {}'.format(i, solution()))