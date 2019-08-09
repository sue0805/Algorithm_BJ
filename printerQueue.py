for _ in range(int(input())):
    n, m = map(int, input().split())
    docs = list(map(int, input().split()))
    target = []
    for i in range(n):
        if i == m:
            target.append(True)
        else:
            target.append(False)
    cnt = 0
    while True:
        tmp = docs[0]
        tmp_t = target[0]
        if docs[0] == max(docs):
            docs.remove(tmp)
            target.remove(tmp_t)
            cnt += 1
            if tmp_t:
                break
        else:
            tmp = docs[0]
            tmp_t = target[0]
            docs.remove(tmp)
            docs.append(tmp)
            target.remove(tmp_t)
            target.append(tmp_t)
    print(cnt)