S = int(input())

cnt = 0
tmp = S
for i in range(1, S):
    tmp -= i
    cnt += 1
    if tmp - 1 < i:
        break
print(cnt)

num = int(input())
sum = 0
numList = []
for i in range(1, num):
    if sum + i <= num:
        numList.append(i)
        sum += i
    elif sum + i > num:
        break
print(len(numList))