keys = ["1qaz", "2wsx", "3edc", "4rfv5tgb", "6yhn7ujm", "8ik,", "9ol.", "0p;/'[]-="]
fingers = [0] * 8

string = list(input().lower())

for ch in string:
    for idx, key in enumerate(keys):
        if key.count(ch) != 0:
            fingers[idx] += 1
            break

for n in fingers:
    print(n)