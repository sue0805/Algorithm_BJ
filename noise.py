import sys

A = int(sys.stdin.readline())
oper = sys.stdin.readline()
B = int(sys.stdin.readline())

print(A * B if "*" in oper else A + B)
