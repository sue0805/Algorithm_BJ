keys = ['`1234567890-=', 'QWERTYUIOP[]\\', 'ASDFGHJKL;\'', 'ZXCVBNM,./']
wrong = ''
for i in range(100):
    line = input()
    if line == '':
        break
    wrong += line + '\n'

right = ''
for ch in wrong:
    if ch == ' ' or ch == '\n':
        right += ch
        continue
    for key in keys:
        if ch in key:
            right += key[key.find(ch)-1]
            break
print(right)
