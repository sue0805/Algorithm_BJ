import math

N = int(input())
count = 0

for i in range(2, int(math.sqrt(N)) + 1):
    if N % i == 0:
        print(N - N // i)
        break
    elif i == int(math.sqrt(N)):
        print(N - 1)