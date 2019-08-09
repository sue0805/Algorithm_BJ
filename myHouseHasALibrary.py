N = int(input())

tmp = 0
maxPrev = 0
maxNext = 0
foundLast = False
for i in range(1, N+1):
    book = int(input())
    if book == N and i == 1:
        print(N - 1)
        break
    elif N == book:
        foundLast = True
    elif not foundLast and book < tmp:
        maxPrev = max(maxPrev, book)
    elif foundLast:
        maxNext = max(maxNext, book)
    tmp = max(tmp, book)

if maxPrev != 0 or maxNext != 0:
    print(max(maxPrev, maxNext))