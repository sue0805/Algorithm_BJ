for _ in range(0, 3):
    time = list(map(int, input().split()))
    start = time[0] * 60 * 60 + time[1] * 60 + time[2]
    end = time[3] * 60 * 60 + time[4] * 60 + time[5]

    result = end - start
    h = result // 60 // 60
    result = result % 3600
    m = result // 60
    result %= 60
    s = result
    print(h, m, s)
