dirs = {
    'R': (0, 1),
    'L': (0, -1),
    'B': (-1, 0),
    'T': (1, 0),
    'RT': (1, 1),
    'LT': (1, -1),
    'RB': (-1, 1),
    'LB': (-1, -1)
}

alpha, num = {}, {}
for i, a in enumerate('ABCDEFGH', 1):
    alpha[a] = i
    num[i] = a

king, stone, n = input().split()
n = int(n)
king = [int(king[1]), alpha[king[0]]]
stone = [int(stone[1]), alpha[stone[0]]]

for i in range(n):
    d = input()
    ky, kx = king[0] + dirs[d][0], king[1] + dirs[d][1]
    sy, sx = stone[0] + dirs[d][0], stone[1] + dirs[d][1]
    if 1 <= ky <= 8 and 1 <= kx <= 8:
        if ky == stone[0] and kx == stone[1]:
            if 1 <= sy <= 8 and 1 <= sx <= 8:
                king = [ky, kx]
                stone = [sy, sx]
            else:
                continue
        else:
            king = [ky, kx]

print(num[king[1]] + str(king[0]))
print(num[stone[1]] + str(stone[0]))
