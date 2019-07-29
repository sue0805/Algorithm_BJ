for _ in range(0, int(input())):
    n, m = input().split()
    n = int(n[::-1])
    m = int(m[::-1])

    print(int(str(n + m)[::-1]))