N = int(input())
ins = list()
for i in range(N):
    ins.append(input())

cnt = 0
for i in range(N):
    order = ins[0]
    out = input()
    if out != order:
        ins.remove(out)
        cnt += 1
    else:
        ins.remove(order)

print(cnt)