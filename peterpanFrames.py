letters = list(input())
width = 4 * len(letters) + 1
height = 5
prev_ch = '#'
char = '#'
arr = [[""] * width for i in range(0, height)]

for i in range(0, width):
    if (i // 4 + 1) % 3 == 0 and i != width - 1:
        char = "*"
        prev_ch = '*'
    else:
        if prev_ch == '#':
            char = '#'
        else:
            char = '*'
            prev_ch = '#'
    for j in range(0, height):
        if i == width - 1 or i % 4 == 0:
            arr[j][i] = '.' if j != 2 else char
        elif i % 4 == 1 or i % 4 == 3:
            arr[j][i] = char if j % 2 == 1 else '.'
        else:
            if j == 2:
                arr[j][i] = letters[i // 4]
            else:
                arr[j][i] = char if j % 4 == 0 else '.'

for a in arr:
    for _ in a:
        print(_, end="")
    print()