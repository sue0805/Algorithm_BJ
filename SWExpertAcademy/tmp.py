def move_microbe():
    for x in range(len(microbes)):
        if microbes[x][0] == -1 and microbes[x][1] == -1:
            pass
        else:
            microbes[x][0] += ways[microbes[x][3]][0]
            microbes[x][1] += ways[microbes[x][3]][1]


def alert_microbe():
    for microbe in microbes:
        if microbe[0] == 0 or microbe[0] == N - 1 or microbe[1] == 0 or microbe[1] == N - 1:
            microbe[2] = int(microbe[2] / 2)
            if microbe[3] % 2:
                microbe[3] += 1
            else:
                microbe[3] -= 1


def check_microbe():
    visited = [0] * len(microbes)
    for x in range(len(microbes) - 1):
        if not visited[x]:
            visited[x] = 1
            tmp = [x]
            for y in range(x + 1, len(microbes)):
                if microbes[x][0] == microbes[y][0] and microbes[x][1] == microbes[y][1]:
                    if not visited[y]:
                        tmp.append(y)
                        visited[y] = 1
            if len(tmp) > 1:
                merge_microbe(tmp)


def merge_microbe(targets):
    max_value = microbes[targets[0]][2]
    max_value_index = targets[0]

    for target in targets:
        if microbes[target][2] > max_value:
            max_value = microbes[target][2]
            max_value_index = target

    for target in targets:
        if target != max_value_index:
            microbes[max_value_index][2] += microbes[target][2]
            microbes[target][0] = -1
            microbes[target][1] = -1


def count_microbes():
    count = 0
    for microbe in microbes:
        if microbe[0] == -1 and microbe[1] == -1:
            pass
        else:
            count += microbe[2]
    print(f"#{tc} {count}")


ways = {
    1: [-1, 0],
    2: [1, 0],
    3: [0, -1],
    4: [0, 1]
}

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())

    microbes = [0] * K
    for i in range(K):
        microbes[i] = list(map(int, input().split()))

    for _ in range(M):
        move_microbe()
        alert_microbe()
        check_microbe()
    count_microbes()
