from itertools import cycle
cy = cycle(range(1, 9))
player = 0
k = int(input())
while player != k:
    player = next(cy)


end_time = 210
time = 0
prev = [0, player-1]
for i in range(int(input())):
    t, answer = input().split()
    t = int(t)
    time += t
    if time > end_time:
        break
    if answer in ['N', 'P']:
        continue
    else:
        player = next(cy)

print(player)