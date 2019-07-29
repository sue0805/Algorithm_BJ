N = int(input())
result = 0
number = len(str(N))

for i in range(0, number):
    if i == number-1:
        result += (N - (10 ** i) + 1) * (i+1)
    else:
        result += 9 * (10 ** i) * (i+1)

print(result)
