import sys

sec = 0
for i in range(0, 4):
    sec += int(sys.stdin.readline())
print(sec // 60)
print(sec % 60)
