N, C = map(int, input().split())

time = set()
for i in range(0, N):
    fire = int(input())
    if fire in time:
        continue
    for j in range(fire, C + 1, fire):
        time.add(j)

print(len(time))