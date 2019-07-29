import math

N, W, H = map(int, input().split())
X = math.sqrt(W * W + H * H)

for i in range(0, N):
    matches = int(input())
    print("DA" if matches <= W or matches <= H or matches <= X else "NE")
