W, K = list(), list()
for i in range(0, 20):
    if i < 10:
        W.append(int(input()))
    else:
        K.append(int(input()))

W.sort(reverse=True)
K.sort(reverse=True)

wsum, ksum = 0, 0

for i in range(0, 3):
    wsum += W[i]
    ksum += K[i]

print(wsum, ksum)
