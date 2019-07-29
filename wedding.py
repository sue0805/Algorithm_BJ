import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

tmp = set()
invite = set()
friend = list()

cnt = 0
for i in range(0, M):
    a, b = map(int, sys.stdin.readline().split())
    if a == 1:
        invite.add(b)
        tmp.add(b)
    elif b == 1:
        invite.add(a)
        tmp.add(a)
    else:
        friend.append([a, b])

for i in friend:
    if i[0] in tmp and i[1] != 1:
        invite.add(i[1])
    elif i[1] in tmp:
        invite.add(i[0])


print(len(invite))
