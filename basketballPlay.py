N = int(input())
players = list()
picked = list()

for i in range(0, N):
    players.append(input())

players.sort()

a = "a"
cnt = 0
ok = False

for i in players:
    if cnt < 5 and i[0] == a:
        cnt += 1
        if cnt == 5:
            print(a, end="")
            ok = True
    elif i[0] != a:
        cnt = 1
        a = i[0]

if not ok:
    print("PREDAJA")