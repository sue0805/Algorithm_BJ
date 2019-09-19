n, k = map(int, input().split())
permu = list(input().split(','))

for i in range(k):
    permu = [str(int(permu[i+1]) - int(permu[i])) for i in range(len(permu) - 1)]

print(','.join(permu))