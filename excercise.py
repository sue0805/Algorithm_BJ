N, m, M, T, R = map(int, input().split())

time = 0
relax = 0
now = m

while True:
    if M - m < T:
        time = -1
        break
    if now + T <= M:
        now += T
        time += 1
    else:
        now = now - R if now - R >= m else m
        relax += 1
    if time == N:
        break

print(time + relax)