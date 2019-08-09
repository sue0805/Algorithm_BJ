N = int(input())
player = list()
rounds = [[], [], []]
for i in range(0, N):
    game = list(map(int, input().split()))
    player.append(game)
    j = 0
    for arr in rounds:
        arr.append(game[j])
        j += 1

for p in player:
    sum = 0
    for i in range(0, 3):
        if rounds[i].count(p[i]) == 1:
            sum += p[i]
    print(sum)