class Microbe:
    def __init__(self, x, y, amount, direction, wall):
        self.x = x
        self.y = y
        self.amount = amount
        self.direction = direction
        self.wall = wall

    def move(self, square, visited):
        d = self.direction
        if d == 1:
            self.x -= 1
            if self.x == 0:
                self.direction = 2
                self.amount //= 2
        elif d == 2:
            self.x += 1
            if self.x == self.wall:
                self.direction = 1
                self.amount //= 2
        elif d == 4:
            self.y += 1
            if self.y == self.wall:
                self.direction = 3
                self.amount //= 2
        elif d == 3:
            self.y -= 1
            if self.y == 0:
                self.direction = 4
                self.amount //= 2

        if self.amount > 0:
            square[self.x][self.y].append(self)
            if len(square[self.x][self.y]) > 1:
                visited.add((self.x, self.y))
        elif self.amount == 0:
            micros.remove(self)

    def meet(self, microbes):
        microbes.sort(key=lambda mic: mic.amount, reverse=True)
        amt = 0
        for microbe in microbes:
            amt += microbe.amount
        return Microbe(self.x, self.y, amt, microbes[0].direction, self.wall)

    def __str__(self):
        return '[{}, {}, {}, {}]'.format(self.x, self.y, self.amount, self.direction)


for _ in range(0, int(input())):
    N, M, K = map(int, input().split())
    micros = []
    for __ in range(0, K):
        x, y, am, di = map(int, input().split())
        m = Microbe(x, y, am, di, N - 1)
        micros.append(m)

    for __ in range(0, M):
        square = []
        visited = set()
        for ___ in range(0, N):
            tmp = []
            for ____ in range(0, N):
                tmp.append(list())
            square.append(tmp)
        for m in micros:
            m.move(square, visited)
        for v in visited:
            for m in square[v[0]][v[1]]:
                micros.remove(m)
            micros.append(square[v[0]][v[1]][0].meet(square[v[0]][v[1]]))

    print('#' + str(_ + 1), sum(m.amount for m in micros))

