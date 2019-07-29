import sys

N = int(sys.stdin.readline())

for i in range(0, N):
    hp, mp, att, dep, hhp, mmp, aatt, ddep = map(int, sys.stdin.readline().split())
    hp = hp + hhp if hp + hhp > 1 else 1
    mp = mp + mmp if mp + mmp > 1 else 1
    att = att + aatt if att + aatt > 0 else 0
    dep += ddep

    print(1 * hp + 5 * mp + 2 * att + 2 *dep)
