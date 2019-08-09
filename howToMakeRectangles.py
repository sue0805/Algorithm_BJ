n = int(input())
result = 0
for i in range(1, (n // 2) + 2):
    for j in range(i, n + 1):
        if i * j <= n:
            result += 1

print(result)