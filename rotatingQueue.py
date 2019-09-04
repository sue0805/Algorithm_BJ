n, m = map(int, input().split())
loc = list(map(int, input().split()))
arr = [0] * n
cnt = 0
for l in loc:
    arr[l-1] = l

while len(loc) != 0:
    idx = arr.index(loc[0])
    if idx == 0:
        arr.pop(0)
        loc.pop(0)
        continue
    elif idx >= len(arr) - idx:
        arr.insert(0, arr.pop())
    else:
        arr.append(arr.pop(0))
    cnt += 1

print(cnt)