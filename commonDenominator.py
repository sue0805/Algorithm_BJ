import sys


def gcd(a, b):
    if a % b != 0:
        result = gcd(b, a % b)
    else:
        return b
    return result


n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

GCD = gcd(nums[0], nums[1]) if n == 2 else gcd(gcd(nums[0], nums[1]), nums[2])

for i in range(1, GCD+ 1):
    if GCD % i == 0:
        print(i)
