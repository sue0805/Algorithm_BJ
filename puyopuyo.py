from operator import itemgetter

row, col = 12, 6
board = [list(input()) for i in range(row)]
visited = [[False] * col for i in range(row)]
dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def find(i, j):
    result = [[i, j]]
    visited[i][j] = True
    for d in dirs:
        y = i + d[0]
        x = j + d[1]
        if 0 <= y < row and 0 <= x < col and board[i][j] == board[y][x] and not visited[y][x]:
            result += find(y, x)
    return result


def fill(i, j):
    global board
    if i - 1 < 0 or board[i - 1][j] == '.':
        board[i][j] = '.'
    else:
        board[i][j] = board[i - 1][j]
        board[i - 1][j] = '.'
        fill(i-1, j)


result = 0
while True:
    visited = [[False] * col for i in range(row)]
    rem = []
    for i in range(row):
        for j in range(col):
            if board[i][j] != '.' and not visited[i][j]:
                tmp = find(i, j)
                if len(tmp) >= 4:
                    rem += tmp
    if not rem:
        break
    result += 1
    rem = sorted(rem, key=itemgetter(0, 1), reverse=True)
    while rem:
        i, j = rem.pop()
        fill(i, j)

print(result)