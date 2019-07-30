N = int(input())
condos = []
cnt = 0
isAll = True
d, c = 0, 0
for i in range(0, N):
    D, C = map(int, input().split())
    condos.append({'d': D, 'c': C})
    if i == 0:
        d, c = D, C
    elif isAll:
        if C < c and D > d:
            continue
        else:
            isAll = False

if isAll:
    print(len(condos))
else:
    for i in range(0, N):
        d1 = condos[i]['d']
        c1 = condos[i]['c']
        candidate = True
        tmp = 0
        for j in range(0, N):
            if i == j:
                continue
            d2 = condos[j]['d']
            c2 = condos[j]['c']

            if d1 > d2 and c1 >= c2 or c1 > c2 and d1 >= d2:
                candidate = False
                break
        if candidate:
            cnt += 1

    print(cnt)