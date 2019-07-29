queue = []


def security_area(x, y, z):
    global house_cnt, queue

    queue.insert(0, [x, y, 1])
    visited[x][y] = True

    while True:
        tmp = queue.pop()
        a, b, c = tmp[0], tmp[1], tmp[2]

        if c > z:
            queue = []
            return

        if city[a][b] == 1:
            house_cnt += 1

        if a + 1 < len(city) and not visited[a + 1][b]:
            queue.insert(0, [a + 1, b, c + 1])
            visited[a + 1][b] = True
        if a - 1 >= 0 and not visited[a - 1][b]:
            queue.insert(0, [a - 1, b, c + 1])
            visited[a - 1][b] = True
        if b + 1 < len(city) and not visited[a][b + 1]:
            queue.insert(0, [a, b + 1, c + 1])
            visited[a][b + 1] = True
        if b - 1 >= 0 and not visited[a][b - 1]:

            queue.insert(0, [a, b - 1, c + 1])
            visited[a][b - 1] = True

        if len(queue) == 0:
            return


def k(num):
    return num ** 2 + (num - 1) ** 2


T = int(input())

for i in range(0, T):
    N, M = map(int, input().split())
    city = list()
    house_cnt = 0
    for j in range(0, N):
        city.append(list(map(int, input().split())))
        house_cnt += city[j].count(1)
    num = N if N % 2 != 0 else N + 1
    K = k(num)
    if house_cnt * M >= K:
        print("#" + str(i+1), house_cnt)
    else:
        result = 0
        isEnd = False
        for z in range(num, 0, -1):
            for x in range(0, N):
                for y in range(0, N):
                    house_cnt = 0
                    visited = list()
                    for f in range(0, N):
                        visited.append([False] * N)
                    security_area(x, y, z)
                    if house_cnt * M >= k(z):
                        result = max(result, house_cnt)

        print("#" + str(i+1), result)
