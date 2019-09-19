n1, n2 = map(int, input().split())
ants = [0] * (n1 + n2)
d = 1
ant1 = input()
ant2 = input()
t = int(input())

i = 0
for ant in ant1[::-1]:
    ants[i] = (ant, 1)
    i += 1

for ant in ant2:
    ants[i] = (ant, -1)
    i += 1

for _ in range(t):
    i = 0
    while i < len(ants) - 1:
        if ants[i][1] == 1 and ants[i+1][1] == -1:
            ants[i], ants[i+1] = ants[i+1], ants[i]
            i += 2
        else:
            i += 1

for ant in ants:
    print(ant[0], end="")