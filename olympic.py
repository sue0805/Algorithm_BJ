import sys
from operator import itemgetter

N, K = map(int, sys.stdin.readline().split())

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
            grade = grade + same if same > 1 else grade + 1
            same = 1 if same > 1 else same
    if i[0] == K:
        break
    tmp = i

print(grade)