import bisect
import sys

direction = {"S": [0, 1], "J": [0, -1], "I": [1, 0], "Z": [-1, 0]}
N, M = map(int, sys.stdin.readline().split())
now = [0, 0]

points_x = []
points_y = []
sum = 0

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    points_x.append(x)
    points_y.append(y)
    sum += abs(x) + abs(y)

orders = sys.stdin.readline().splitlines()[0]

points_x.sort()
points_y.sort()

for order in orders:
    d = direction[order]
    now[0] += d[0]
    now[1] += d[1]
    if order == 'S' or order == 'J':
        if order == 'S':
            idx = bisect.bisect_left(points_y, now[1])
            sum += (idx - 1) + (-1 * (N-1-idx))
        else:
            idx = bisect.bisect_right(points_y, now[1])
            sum += -1 * (idx - 1) + (N-1-idx)
        print(sum)
    elif order == 'I' or order == 'Z':
        if order == 'I':
            idx = bisect.bisect_left(points_x, now[0])
            sum += (idx - 1) + (-1 * (N-1-idx))
        else:
            idx = bisect.bisect_right(points_x, now[0])
            sum += -1 * (idx - 1) + (N-1-idx)
        print(sum)