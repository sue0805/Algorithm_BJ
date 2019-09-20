def rotate(idx, dir):
    visited[idx] = True
    if idx - 1 >= 0 and gears[idx-1][2] != gears[idx][6] and not visited[idx-1]:
        rotate(idx-1, -dir)
    if idx + 1 < 4 and gears[idx+1][6] != gears[idx][2] and not visited[idx+1]:
        rotate(idx+1, -dir)

    if dir == 1:
        gears[idx].insert(0, gears[idx].pop())
    else:
        gears[idx].append(gears[idx].pop(0))


gears = [list(input()) for _ in range(4)]
visited = [False] * 4

for i in range(int(input())):
    r, d = map(int, input().split())
    rotate(r - 1, d)
    visited = [False] * 4

score = 0
for i in range(4):
    score += int(gears[i][0]) * (2 ** i)

print(score)