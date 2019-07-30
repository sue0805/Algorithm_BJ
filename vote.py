N, M = map(int, input().split())
costs = []
plays = [0] * N
for i in range(0, N):
    costs.append(int(input()))

for i in range(0, M):
    man = int(input())
    for idx, c in enumerate(costs):
        if c <= man:
            plays[idx] += 1
            break

print(plays.index(max(plays)) + 1)