for _ in range(int(input())):
    isReal = True
    words = {}
    message = input()
    for i in range(len(message)):
        words[message[i]] = words[message[i]] + 1 if message[i] in words else 1
        if words[message[i]] == 3:
            if i+1 > len(message) - 1 or message[i+1] != message[i]:
                isReal = False
                break
            elif message[i+1] == message[i]:
                words[message[i]] = -1
    print("OK" if isReal else "FAKE")