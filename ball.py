cups = [1, 2, 3]

for i in range(int(input())):
    a, b = map(int, input().split())
    idxA = cups.index(a)
    idxB = cups.index(b)
    cups[idxA], cups[idxB] = b, a

print(cups[0])