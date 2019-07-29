import sys

score = 0
for i in range(0, 10):
    mushroom = int(sys.stdin.readline())
    if abs(100 - score) >= abs(100 - (score + mushroom)):
        score += mushroom
    else:
        break
print(score)
