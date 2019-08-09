N, B, H, W = map(int, input().split())
minBudget = 500001
for _ in range(H):
    cost = int(input())
    weeks = [N * cost for i in list(map(int, input().split())) if i >= N and N * cost <= B]
    for w in weeks:
        minBudget = min(minBudget, w)

print(minBudget if minBudget < B else 'stay home')