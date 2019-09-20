dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dir_alpha = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
orders = {"L": -1, "R": 1}

a, b = map(int, input().split())
n, m = map(int, input().split())

robot = {}

for i in range(1, n+1):
    x, y, d = input().split()
    x, y = map(int, [x, y])
    robot[i] = {'now' : [y, x], 'dir' : dir_alpha[d]}


def find(i, j, no):
    for r in robot:
        if r == no:
            continue
        y, x = robot[r]['now']
        if y == i and x == j:
            print('Robot {} crashes into robot {}'.format(no, r))
            exit(0)


for i in range(m):
    no, order, cnt = input().split()
    no, cnt = map(int, [no, cnt])
    for j in range(cnt):
        if order in orders:
            d = robot[no]['dir'] + orders[order]
            if d < 0:
                d = 3
            elif d > 3:
                d = 0
            robot[no]['dir'] = d
        else:
            d = robot[no]['dir']
            y, x = robot[no]['now']
            y += dirs[d][0]
            x += dirs[d][1]
            if 1 <= y <= b and 1 <= x <= a:
                robot[no]['now'] = [y, x]
                find(y, x, no)
            else:
                print('Robot {} crashes into the wall'.format(no))
                exit(0)

print('OK')
