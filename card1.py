from collections import deque
n = int(input())
dq = deque([i for i in range(1, n+1)])
while dq:
    print(dq.popleft(), end=" ")
    if len(dq) == 0:
        break
    dq.append(dq.popleft())