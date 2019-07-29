x1, x2, y1, y2 = 100, 1, 100, 1
for _ in range(0, int(input())):
    x, y = map(int, input().split())
    x1 = min(x1, x)
    x2 = max(x2, x)
    y1 = min(y1, y)
    y2 = max(y2, y)

print(pow(max(x2 - x1, y2 - y1), 2))