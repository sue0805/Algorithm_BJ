N = int(input())
arr = list(map(int, input().split()))
arr = [arr[i-1] * i for i in range(1, N+1)]

tmp = 0
print(arr[0], end=" ")
for i in range(1, N):
    tmp += arr[i - 1]
    arr[i] -= tmp
    print(arr[i], end=" ")

