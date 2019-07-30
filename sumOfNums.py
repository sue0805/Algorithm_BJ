S = int(input())

tmp, i = S, 0
for i in range(1, S):
    tmp -= i
    if tmp - 1 < i:
        break
print(i)