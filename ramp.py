n, l = map(int, input().split())
roads = [list() for i in range(n)]
ramps = []
result = 0
for i in range(n):
    roads[i] = list(map(int, input().split()))


def find_Y(i, j, prev, find_right, before):
    global result
    r = roads[i][j]
    if prev == r:
        if find_right and len(before) == l:
            before = []
            find_right = False
        before += [(i, j)]
        if find_right and len(before) == l:
            before = []
            find_right = False
    else:
        if find_right:
            if len(before) == l:
                before = []
                find_right = False
            else:
                return
        if abs(prev - r) == 1:
            if prev > r:
                find_right = True
            else:
                if len(before) >= l:
                    pass
                else:
                    return
            if (i, j) not in ramps:
                before = [(i, j)]
            else:
                before = []
        else:
            # print(j)
            return
    if i + 1 < n:
        find_Y(i+1, j,roads[i][j], find_right, before)
    else:
        if find_right and len(before) != l:
            return
        else:
            # print(j)
            result += 1



def find_X(i, j, prev, find_right, before):
    global result
    r = roads[i][j]
    if prev == r:
        if find_right and len(before) == l:
            before = []
            find_right = False
        before += [(i, j)]
        if find_right and len(before) == l:
            before = []
            find_right = False
    else:
        if find_right:
            if len(before) == l:
                before = []
                find_right = False
            else:
                return
        if abs(prev - r) == 1:
            if prev > r:
                find_right = True
            else:
                if len(before) >= l:
                    pass
                else:
                    return
            if (i, j) not in ramps:
                before = [(i, j)]
            else:
                before = []
        else:
            return
    if j + 1 < n:
        find_X(i, j+1, roads[i][j], find_right, before)
    else:
        if find_right and len(before) != l:
            return
        else:
            result += 1


for i in range(n):
    find_Y(0, i, roads[0][i], False, [])
    find_X(i, 0, roads[i][0], False, [])

print(result)