N, K = map(int, input().split())
number = len(str(N))
arr = [0] * number
result = -1

for i in range(0, number):
    if i == number-1:
        arr[i] = (N - (10 ** i) + 1) * (i+1) + arr[i - 1]
    else:
        arr[i] = 9 * (10 ** i) * (i+1) + arr[i - 1]

    if arr[i] >= K:
        if i == 0:
            result = K
        else:
            result = int('9' * i)
            result += (K - arr[i - 1]) // (i + 1) + 1
            if (K - arr[i - 1]) % (i+1) == 0:
                result -= 1
            result = int(str(result)[(K - arr[i - 1]) % (i + 1) - 1])
        break

print(result)