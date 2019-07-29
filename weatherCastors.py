H, W = map(int, input().split())

forecasts = [[-1] * W for i in range(0, H)]
time = 100
for i in range(0, H):
    clouds = list(input())
    for idx, j in enumerate(clouds):
        if j == "c":
            forecasts[i][idx] = 0
            if idx + 1 < W and clouds[idx + 1] != "c":
                time = 0
                for k in range(idx + 1, W):
                    time += 1
                    forecasts[i][k] = time
    for cast in forecasts[i]:
        print(cast, end=" ")
    print()