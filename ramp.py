n, l = map(int, input().split())
roads = []
ramps = []
result = 0

for i in range(n):
    row = list(map(int, input().split()))
    roads.append(row)
    prev = 0
    tmp = []
    cnt = 0
    rampCnt = False
    canGo = True
    for j in range(n):
        # 같은 층이고 경사로가 없으면 카운트
        if rampCnt:
            if cnt == l:
                cnt, tmp = 0, []
            else:
                if prev == row[j]:
                    if [i, j] not in ramps:
                        cnt += 1
                        tmp.append([i, j])
                    else:
                        break
                else:
                    break
        else:
            if prev == row[j]:
                if [i, j] not in ramps:
                    cnt += 1
                    tmp.append([i, j])
                else:
                    cnt, tmp = 0, []
            else:
                if abs(row[j] - prev) == 1:
                    if row[j] > prev:
                        if cnt >= l:
                            ramps.extend(tmp[l-cnt:])
                            cnt, tmp = 1, [[i, j]]
        prev = row[j]
    print()
print()
print(result)