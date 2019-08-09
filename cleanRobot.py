import sys
sys.setrecursionlimit(1000000)

N, M = map(int, input().split())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
now = list(map(int, input().split()))
area = [list(map(int, input().split())) for _ in range(N)]
cleaned = [[False] * M for _ in range(N)]
counter = 0


def clean(y, x, cnt):
    global cleaned, area, now, dx, dy, counter

    if area[y][x] != 1 and not cleaned[y][x]:
        cleaned[y][x] = True
        counter += 1

    left = now[2] - 1 if now[2] - 1 >= 0 else 3
    y += dy[left]
    x += dx[left]
    if 0 <= y < N and 0 <= x < M and not cleaned[y][x] and area[y][x] != 1:
        now = [y, x, left]
        clean(y, x, 0)
    elif y < 0 or y >= N or x < 0 or x >= M or cleaned[y][x] or area[y][x] == 1:
        cnt += 1
        if cnt <= 4:
            now[2] = left
            clean(now[0], now[1], cnt)
        else:
            y = now[0] - dy[now[2]]
            x = now[1] - dx[now[2]]
            if 0 <= y < N and 0 <= x < M and area[y][x] != 1:
                now = [y, x, now[2]]
                clean(y, x, 0)
            else:
                return


clean(now[0], now[1], 0)
print(counter)
