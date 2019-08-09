A, B = input().split()
A = list(A)
B = list(B)

same = set(A) & set(B)
word = same.pop()
idx = A.index(word)

for w in same:
    tmp = A.index(w)
    if idx > tmp:
        idx = tmp
        word = w

x = idx
y = B.index(word)

for i in range(0, len(B)):
    if i == y:
        for a in A:
            print(a, end="")
        print()
    else:
        print("." * x + B[i] + "." * (len(A) - x - 1))