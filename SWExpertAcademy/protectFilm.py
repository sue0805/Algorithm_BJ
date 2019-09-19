def solution():
    result = [100]
    d, w, k = map(int, input().split())
    film = [list() for i in range(d)]
    checked = {}
    for i in range(d):
        film[i] = list(map(int, input().split()))

    def check(ab, a=[]):
        ck = True
        for j in range(w):
            cnt = 1
            prev = film[0][j] if 0 not in a else ab
            for i in range(1, d):
                f = film[i][j]
                if i in a:
                    f = ab
                if prev == f:
                    cnt += 1
                    if cnt >= k:
                        break
                else:
                    cnt = 1
                prev = f
            if cnt < k:
                ck = False
                break
        return ck

    def dfs(a, i, ab):
        flag = False
        ta = tuple(a)
        if (ta, ab) in checked:
            flag = checked[(ta, ab)]
            if flag:
                return
        else:
            flag = check(ab, a)
            checked[(ta, ab)] = flag
        if flag:
            result[0] = min(result[0], len(a))
        if i >= len(film):
            return
        dfs(a, i+1, ab)
        dfs(a + [i], i+1, ab)

    for i in range(2):
        dfs([], 0, i)
    return result[0]


for i in range(1, int(input())+1):
    print('#{} {}'.format(i, solution()))