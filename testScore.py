import sys

S = sum(map(int, sys.stdin.readline().split()))
T = sum(map(int, sys.stdin.readline().split()))

print(S if S >= T else T)