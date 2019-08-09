sticks = [64]
x = int(input())
cnt = 0
while sum(sticks) != x:
    cnt += 1
    if sum(sticks) > x:
        sticks[-1] = sticks[-1] // 2
        if sum(sticks) < x:
            sticks.append(sticks[-1])

print(len(sticks))