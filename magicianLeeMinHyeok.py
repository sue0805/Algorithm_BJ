R, C = map(int, input().split())

R *= 2
C *= 2

card = [""] * R
for i in range(0, R // 2):
    pattern = list(input().split())
    for p in pattern:
        tmp = p + p[::-1]
        card[i] = list(tmp)
        card[R - 1 - i] = list(tmp)


def error(a, b):
    global card
    if card[a][b] == "#":
        card[a][b] = "."
    else:
        card[a][b] = '#'


a, b = map(int, input().split())
error(a-1, b-1)

for c in card:
    for w in c:
        print(w, end="")
    print()
