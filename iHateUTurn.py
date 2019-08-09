R, C = map(int, input().split())
check = [[False] * C for i in range(R)]
city_map = [list(input()) for i in range(R)]
uturn = False

for i, row in enumerate(city_map):
    for j, road in enumerate(row):
        cnt = 0
        if road == '.' and not check[i][j]:
            check[i][j] = True
            if i + 1 < R and city_map[i+1][j] == '.':
                cnt += 1
            if i - 1 >= 0 and city_map[i-1][j] == '.':
                cnt += 1
            if j + 1 < C and city_map[i][j+1] == '.':
                cnt += 1
            if j - 1 >= 0 and city_map[i][j-1] == '.':
                cnt += 1
        if cnt == 1:
            uturn = True
            break
    if uturn:
        break

print(0 if not uturn else 1)