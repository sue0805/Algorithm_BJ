n = int(input())
for i in range(1, 8):
    if n > pow(10, i):
        if str(n % pow(10, i))[0] == '5':
            n += 1 * pow(10, i - 1)
        n = round(n, -1 * i)
    else:
        break
print(n)