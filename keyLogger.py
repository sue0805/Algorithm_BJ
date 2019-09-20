import sys
for i in range(int(sys.stdin.readline())):
    tc = sys.stdin.readline().strip()
    left, right = [], []
    for t in tc:
        if t == '<' and right:
            left.append(right.pop())
        elif t == '>' and left:
            right.append(left.pop())
        elif t == '-' and right:
            right.pop()
        elif t not in ['<', '>', '-']:
            right.append(t)
    print(''.join(right + left[::-1]))