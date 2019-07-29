import sys

cafes = list()
result = -1


def cafe_tour(x, y, cnt, visited, home, size, direction):
    global result
    if x == home[0] and y == home[1] and len(visited) != 0:
        result = max(result, cnt)
        return
    if cafes[x][y] in visited:
        return
    if y != home[1] and x == home[0]:
        return
    if direction == "r":
        if x + 1 < size and y + 1 < size:
            cafe_tour(x + 1, y + 1, cnt + 1, visited + [cafes[x][y]], home, size, "r")
        if x + 1 < size and y - 1 >= 0 and len(visited) > 0:
            cafe_tour(x + 1, y - 1, cnt + 1, visited + [cafes[x][y]], home, size, "d")
    elif direction == "d":
        if x + 1 < size and y - 1 >= 0:
            cafe_tour(x + 1, y - 1, cnt + 1, visited + [cafes[x][y]], home, size, "d")
        if x - 1 >= 0 and y - 1 >= 0:
            cafe_tour(x - 1, y - 1, cnt + 1, visited + [cafes[x][y]], home, size, "l")
    elif direction == "l":
        if x - 1 >= 0 and y - 1 >= 0:
            cafe_tour(x - 1, y - 1, cnt + 1, visited + [cafes[x][y]], home, size, "l")
        if x - 1 >= 0 and y + 1 < size:
            cafe_tour(x - 1, y + 1, cnt + 1, visited + [cafes[x][y]], home, size, "t")
    elif x - 1 >= 0 and y + 1 < size and direction == "t":
        cafe_tour(x - 1, y + 1, cnt + 1, visited + [cafes[x][y]], home, size, "t")


T = int(sys.stdin.readline())
for i in range(0, T):
    N = int(sys.stdin.readline())
    cafes = list()
    result = -1
    for j in range(0, N):
        cafes.append(list(map(int, sys.stdin.readline().split())))
    for j in range(1, N - 1):
        for k in range(0, N - 2):
            cafe_tour(k, j, 0, [], [k, j], N, "r")
    print(result)
