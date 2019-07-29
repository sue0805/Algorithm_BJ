result = 0
for _ in range(0, int(input())):
    n = input()
    result += pow(int(n[0:len(n)-1]), int(n[len(n)-1:]))
print(result)