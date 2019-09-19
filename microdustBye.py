from collections import defaultdict, deque

R, C, T = map(int, input().split())
area = [list(map(int, input().split())) for i in range(R)]
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
machine = [(-1, -1), (-1, -1)]

for i in range(R):
    for j in range(C):
        if area[i][j] == -1:
            machine[0] = (i, j)
            machine[1] = [i+1, j]
            break
    if area[i][j] == -1:
        break

while T > 0:
    dustcnt = defaultdict(int)
    for i in range(R):
        for j in range(C):
            if area[i][j] > 0:
                dust = area[i][j]
                cnt = 0
                for d in dirs:
                    ax, ay = i + d[0], j + d[1]
                    if 0 <= ax < R and 0 <= ay < C and area[ax][ay] >= 0:
                        dustcnt[(ax, ay)] += dust // 5
                        cnt += 1
                area[i][j] -= (dust // 5) * cnt

    for dc in dustcnt:
        x, y = dc
        area[x][y] += dustcnt[dc]

    for idx, m in enumerate(machine):
        x, y = m
        x_, y_ = x, y
        if idx == 0:
            arr = deque([0] + area[x][y+1:C] + [area[i][C-1] for i in range(x-1, 0, -1)] + area[0][::-1] + [area[i][0] for i in range(1, x)] + area[x][:y])
            arr.pop()
            d = 0
            while arr:
                x_, y_ = x_ + dirs[d][0], y_ + dirs[d][1]
                if 0 <= x_ < R and 0 <= y_ < C:
                    area[x_][y_] = arr.popleft()
                else:
                    x_, y_ = x_ - dirs[d][0], y_ - dirs[d][1]
                    d = d + 1 if d + 1 <= 3 else 0
        else:
            arr = deque([0] + area[x][y+1:C] + [area[i][C-1] for i in range(x+1, R-1)] + area[R-1][::-1] + [area[i][0] for i in range(R-2, x, -1)] + area[x][:y])
            arr.pop()
            d = 0
            while arr:
                x_, y_ = x_ + dirs[d][0], y_ + dirs[d][1]
                if 0 <= x_ < R and 0 <= y_ < C:
                    area[x_][y_] = arr.popleft()
                else:
                    x_, y_ = x_ - dirs[d][0], y_ - dirs[d][1]
                    d = d - 1 if d - 1 >= 0 else 3
    T -= 1

total = 2
for a in area:
    total += sum(a)
print(total)