import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    N = int(sys.stdin.readline())
    csum = 0
    gsum = 0
    for j in range(0, N):
        C, G = map(float, sys.stdin.readline().split())
        csum += C
        gsum += G * C
    print("{sum} {GPA:.1f}".format(sum=int(csum), GPA=(gsum/csum)))

