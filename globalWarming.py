R, C = map(int, input().split())
sea_map = []
land = []
for i in range(0, R):
    row = list(input())
    sea_map.append(row)
    if row.count('X') == 0:
        continue
    for idx, s in enumerate(row):
        if s == 'X':
            land.append([i, idx])

min_x = 100
min_y = 100
max_x = 0
max_y = 0

for i in range(len(land) - 1, -1, -1):
    x, y = land[i]
    cnt = 0
    if x + 1 == R or sea_map[x + 1][y] == ".":
        cnt += 1
    if x - 1 < 0 or sea_map[x - 1][y] == ".":
        cnt += 1
    if y + 1 == C or sea_map[x][y + 1] == ".":
        cnt += 1
    if y - 1 < 0 or sea_map[x][y - 1] == ".":
        cnt += 1

    if cnt < 3:
        land.remove(land[i])
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        max_x = max(max_x, x)
        max_y = max(max_y, y)

for l in land:
    x, y = l
    sea_map[x][y] = "."

for s in sea_map[min_x:max_x+1]:
    for m in s[min_y:max_y+1]:
        print(m, end="")
    print()