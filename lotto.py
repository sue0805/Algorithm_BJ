from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    line = list(map(int, input().split()))[1:]
    line.sort()
    if not line:
        break
    nums = combinations(line, 6)
    while True:
        try:
            num = next(nums)
            for n in num:
                print(n, end=" ")
            print()
        except StopIteration:
            break
    print()