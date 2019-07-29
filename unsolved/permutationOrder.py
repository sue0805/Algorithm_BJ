N = int(input())
nums = list(map(int, input().split()))
numArr = [num for num in range(1, N + 1)]

if nums[0] == 1:
    numArr = [num for num in range(1, N + 1)]
else:
    numArr = [num for num in nums[1:]]

print(numArr)
sfgsd