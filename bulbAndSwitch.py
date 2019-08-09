N = int(input())
bulbs = list(map(int, input()))
goal = list(map(int, input()))
counter = -1


def switch(start):
    global bulbs, counter
    tmp = bulbs[:]
    cnt = 0
    for i in range(start, N):
        if not(i > 0 and tmp[i - 1] == goal[i - 1]):
            cnt += 1
            if i > 0:
                tmp[i - 1] = 1 if tmp[i-1] == 0 else 0
            if i < N - 1:
                tmp[i + 1] = 1 if tmp[i+1] == 0 else 0
            tmp[i] = 1 if tmp[i] == 0 else 0
        if i == N - 1 and tmp == goal:
            counter = cnt if counter == -1 else min(counter, cnt)
            break


switch(0)
switch(1)

print(counter)
