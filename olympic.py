import sys
from operator import itemgetter

N, K = sys.stdin.readline().split()
N = int(N)
K = int(K)

country = list()

for i in range(0, N):
    country.append(list(map(int, sys.stdin.readline().split())))

country.sort(key=itemgetter(1, 2, 3), reverse=True)

tmp, grade, same = 0, 1, 1

for i in country:
    if tmp == 0:
        tmp = i
    else:
        if i[1] == tmp[1] and i[2] == tmp[2] and i[3] == tmp[3]:
            same += 1
        else:
            if same > 1:
                grade += same
                same = 1
            else:
                grade += 1
    if i[0] == K:
        print(grade)
        break
    tmp = i
