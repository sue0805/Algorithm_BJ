train = 0
maxPassenger = 0
for i in range(4):
    out, enter = map(int, input().split())
    train -= out
    train += enter
    maxPassenger = max(maxPassenger, train)

print(maxPassenger)