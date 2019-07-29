import sys
li = list()
for i in range(0, 5):
    li.append(int(sys.stdin.readline()))

xcost = li[0] * li[4]
ycost = li[1]

if li[4] > li[2]:
    ycost += (li[4] - li[2]) * li[3]

if ycost > xcost:
    print(xcost)
else:
    print(ycost)