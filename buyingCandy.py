C, K = map(int, input().split())

bill = pow(10, K)
left = C % bill * pow(10, K * -1)
left = round(0.6 if left >= 0.5 else left)
cost = C // bill * bill + left * bill
print(int(cost))