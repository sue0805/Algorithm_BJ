vacation = int(input())
language = int(input())
math = int(input())
maxLan = int(input())
maxMath = int(input())

for i in range(0, vacation):
    language -= maxLan
    math -= maxMath
    if language <= 0 and math <= 0:
        print(vacation - i - 1)
        break
