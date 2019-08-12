fibo = [0, 1]


def fiboX(n):
    global fibo
    if 0 <= abs(n) <= 1:
        result = fibo[abs(n)]
    else:
        result = 0
        for i in range(2, abs(n) + 1):
            result = (fibo[0] + fibo[1]) % 1000000000
            fibo[0], fibo[1] = fibo[1], result

    if n < 0 and abs(n) % 2 == 0:
        print(-1)
    elif n == 0:
        print(0)
    else:
        print(1)

    return result


n = int(input())

print(fiboX(n))
