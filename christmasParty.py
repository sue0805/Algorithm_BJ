N = int(input())
M = int(input())
targets = list(map(int, input().split()))
player = [0] * N

for i in range(0, M):
    target = targets[i]
    guess = list(map(int, input().split()))
    for j in range(0, N):
        if guess[j] == target:
            player[j] += 1
        else:
            player[target - 1] += 1

for p in player:
    print(p)