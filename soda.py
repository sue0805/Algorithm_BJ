import sys

e, f, c = map(int, sys.stdin.readline().split())
empty = e + f

newSoda = 0

while empty >= c:
    newSoda += empty // c
    empty = (empty // c) + (empty % c)

print(newSoda)
