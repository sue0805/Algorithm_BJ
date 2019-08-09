import sys


class Counter:
    def __init__(self, j, i, o):
        self.j = j
        self.i = i
        self.o = o

    def __str__(self):
        return "{} {} {}".format(self.j, self.o, self.i)

    def add(self, other):
        self.j += other.j
        self.i += other.i
        self.o += other.o

    def minus(self, other):
        self.j -= other.j
        self.i -= other.i
        self.o -= other.o


planet_map = {}
M, N = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

for i in range(M):
    line = list(sys.stdin.readline())
    J = I = O = 0
    for j in range(N):
        if line[j] == 'J':
            J += 1
        elif line[j] == 'I':
            I += 1
        else:
            O += 1
        planet_map[(i, j)] = Counter(J, I, O)
        if i != 0:
            planet_map[(i, j)].add(planet_map[(i-1, j)])

for _ in range(K):
    a, b, x, y = map(int, input().split())
    cnt = planet_map[(x - 1, y - 1)]
    tmp = Counter(cnt.j, cnt.i, cnt.o)
    if a - 2 >= 0:
        tmp.minus(planet_map[(a - 2, y - 1)])
    if b - 2 >= 0:
        tmp.minus(planet_map[(x - 1, b - 2)])
    if a - 2 >= 0 and b - 2 >= 0:
        tmp.add(planet_map[(a - 2, b - 2)])

    print(tmp)
