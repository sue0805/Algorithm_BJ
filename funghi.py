mushrooms = [int(input()) for _ in range(8)]
result = -1
for i in range(8):
    tmp = 0
    for j in range(4):
        tmp += mushrooms[i-j]
    result = max(result, tmp)
print(result)