scores = list()
for i in range(0, 8):
    scores.append([i+1, int(input())])
scores.sort(key=lambda arr: arr[1])

sum = 0

questions = list()

for i in range(0, 5):
    tmp = scores.pop()
    sum += tmp[1]
    questions.append(tmp[0])

questions.sort()

print(sum)

for i in questions:
    print(str(i), end=' ')
