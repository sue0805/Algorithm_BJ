N = int(input())
count = 0
for i in range(N-1, 0, -1):
    count += 1
    if N % i == 0:
        break
print(count)