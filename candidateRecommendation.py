n = int(input())
recs = int(input())
students = [0] * 101
recommends = list(map(int, input().split()))
photos = []

for r in recommends:
    if r in photos:
        students[r] += 1
    elif len(photos) < n:
        photos.append(r)
        students[r] += 1
    else:
        minR = photos[0]
        for p in photos:
            if students[minR] > students[p]:
                minR = p
        photos.remove(minR)
        students[minR] = 0
        photos.append(r)
        students[r] += 1

photos = sorted(photos)
for p in photos:
    print(p, end=" ")