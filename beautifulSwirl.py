r1, c1, r2, c2 = map(int, input().split())
row = r2 - r1 + 1
col = c2 - c1 + 1

square = [[0] * col for i in range(0, row)]

i, x, y, z = 1, (0 - r1), (0 - c1), 0
cnt = 0
if not(x > row - 1 or y > col - 1 or x < 0 or y < 0):
    square[x][y] = i
    cnt += 1

direction = [1, -1, -1, 1]
d = -1
biggest = 0
loop = 1
while cnt < row * col:
    z += loop % 2
    loop += 1
    d = 0 if d + 1 > 3 else d + 1
    for j in range(0, z):
        if d == 0 or d == 2:
            if x > row - 1 or x < 0:
                y += direction[d] * z
                i += z
                break
            else:
                i += 1
                y += direction[d]
        else:
            if y > col - 1 or y < 0:
                x += direction[d] * z
                i += z
                break
            else:
                i += 1
                x += direction[d]
        if not (x > row - 1 or y > col - 1 or x < 0 or y < 0):
            square[x][y] = i
            cnt += 1
            biggest = max(biggest, len(str(i)))

for arr in square:
    for n in arr:
        print(format(n, str(biggest) + "d"), end=" ")
    print()