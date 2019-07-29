N = int(input())
nums = list(map(int, input().split()))
numArr = [num for num in range(1, N + 1)]


def nn(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


if nums[0] == 1:
    numArr = [num for num in range(1, N + 1)]
    tmpArr = []
    cnt = nums[1] - 1
    while len(numArr) > 0:
        N -= 1
        for n in numArr:
            tmp = numArr.index(n)
            x = tmp * nn(N)
            if x <= cnt < (tmp + 1) * nn(N):
                numArr.remove(n)
                tmpArr.append(n)
                cnt -= x
                break
    for n in tmpArr:
        print(n, end=" ")

else:
    numArr = [num for num in nums[1:]]
    tmpArr = sorted(numArr)
    cnt = 1
    i = 0
    for n in numArr:
        N -= 1
        tmp = tmpArr.index(n)
        tmpArr.remove(n)
        cnt += tmp * nn(N)
        i += 1
    print(cnt)