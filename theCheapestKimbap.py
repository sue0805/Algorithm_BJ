prices = list()
prices.append(tuple(map(int, input().split())))

for i in range(0, int(input())):
    prices.append(tuple(map(int, input().split())))

prices.sort(key=lambda t: t[1] / t[0], reverse=True)

print(format(1000 / prices[0][1] * prices[0][0], ".2f"))