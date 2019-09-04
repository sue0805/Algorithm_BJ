def find_chess(i, j, color, count, result):
    if count == 7:
        repaints.append(min(result, 64-result))
        return

    next_color = 'W' if color == 'B' else 'B'
    cnt = result
    for x in range(i + 1, i + 8 - count):
        if board[x][j] != next_color:
            cnt += 1
        next_color = 'W' if next_color == 'B' else 'B'

    next_color = 'W' if color == 'B' else 'B'
    for x in range(j + 1, j + 8 - count):
        if board[i][x] != next_color:
            cnt += 1
        next_color = 'W' if next_color == 'B' else 'B'

    if count < 7:
        if board[i + 1][j + 1] != color:
            cnt += 1
        find_chess(i + 1, j + 1, color, count + 1, cnt)


n, m = map(int, input().split())
board = []
repaints = []
for i in range(n):
    board.append(list(input()))

for i in range(n - 7):
    for j in range(m - 7):
        find_chess(i, j, board[i][j], 0, 0)

print(min(repaints))
