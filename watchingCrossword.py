R, C = map(int, input().split())
hor_words = []
tmp = [""] * C
ver_words = []
for i in range(R):
    line = input()
    if not '#' in line:
        hor_words.append(line)
    else:
        arr = line.split('#')
        for a in arr:
            if len(a) >= 2:
                hor_words.append(a)
    for j in range(C):
        if line[j] == '#':
            if len(tmp[j]) >= 2:
                ver_words.append(tmp[j])
            tmp[j] = ""
        elif line[j] != '#':
            tmp[j] += line[j]
            if i == R-1 and len(tmp[j]) >= 2:
                ver_words.append(tmp[j])
result = hor_words + ver_words
result.sort()
print(result[0])