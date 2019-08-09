n, m, x, y, k = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]
now = [x, y]
dir = [[0, 0], [0, 1], [0, -1], [-1, 0], [1, 0]]
orders = list(map(int, input().split()))
diceY = [0] * 3
diceX = [0] * 3

for order in orders:
    if 0 <= now[0] + dir[order][0] < n and 0 <= now[1] + dir[order][1] < m:
        now[0] += dir[order][0]
        now[1] += dir[order][1]
        print(diceX, diceY)
        if dir[order][1] < 0:
            diceX.append(diceX.pop(0))
        elif dir[order][1] > 0:
            diceX.insert(0, diceX.pop())
        elif dir[order][0] < 0:
            diceY.append(diceX.pop(1))
            diceX.insert(1, diceY.pop(0))
        elif dir[order][0] > 0:
            diceY.insert(0, diceX.pop(1))
            diceX.insert(1, diceY.pop())
        if area[now[0]][now[1]] == 0:
            if order <= 2:
                area[now[0]][now[1]] = diceX[0]
            else:
                area[now[0]][now[1]] = diceY[1]
        else:
            if order <= 2:
                diceX[0] = area[now[0]][now[1]]
            else:
                diceY[1] = area[now[0]][now[1]]
            area[now[0]][now[1]] = 0
        print(diceX, diceY)
        print(diceX[1])
        print()
    else:
        continue

print(area)
print(orders)
