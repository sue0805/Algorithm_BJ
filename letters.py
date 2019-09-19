import sys
input = sys.stdin.readline


def num(s):
    return ord(s) - 65


r, c = map(int, input().split())
board = [list(map(num, input().rstrip())) for i in range(r)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
max_cnt = 0
check = [False] * 26


def dfs(x, y, cnt):
    global max_cnt
    for d in dirs:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < r and 0 <= ny < c and not check[board[nx][ny]]:
            tmp = board[nx][ny]
            check[tmp] = True
            dfs(nx, ny, cnt + 1)
            check[tmp] = False
    max_cnt = max(max_cnt, cnt)


check[board[0][0]] = True
dfs(0, 0, 1)
print(max_cnt)