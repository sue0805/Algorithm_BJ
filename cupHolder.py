N = int(input())
tmp = list(input())
seats = []
couple = 0
for s in tmp:
    if couple == 1:
        couple = 0
        continue
    if s == "L":
        couple = 1
        seats.extend([0, "A", "A"])
    else:
        seats.extend([0, "A"])
seats.append(0)

seats[0] = 1
seats[1] = "B"
cnt = 1
for idx, s in enumerate(seats):
    if s == 0:
        if seats[idx - 1] == "A":
            seats[idx] = 1
            seats[idx - 1] = "B"
        elif idx + 1 < N and seats[idx + 1] == "A":
            seats[idx] = 1
            seats[idx + 1] = "B"
        else:
            continue
        cnt += 1

print(cnt)