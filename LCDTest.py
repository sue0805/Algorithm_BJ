def test(nums):
    for i in range(5):
        if i % 2 == 0:
            for n in nums:
                print(n[i], end=" ")
        else:
            for _ in range(s):
                for n in nums:
                    print(n[i], end=" ")
                if _ != s - 1:
                    print()
        print()


s, num = map(int, input().split())
square = [[[""] * (s + 2) for i in range(0, 2 * s + 3)]]
w, h = s + 2, 2 * s + 3

left_bar = "|" + " " * (w - 1)
right_bar = " " * (w - 1) + "|"
side_bars = "|" + " " * (w - 2) + "|"
empty = " " * w
line = " " + "-" * s + " "

one = [empty, right_bar, empty, right_bar, empty]
two = [line, right_bar, line, left_bar, line]
three = [line, right_bar, line, right_bar, line]
four = [empty, side_bars, line, right_bar, empty]
five = [line, left_bar, line, right_bar, line]
six = [line, left_bar, line, side_bars, line]
seven = [line, right_bar, empty, right_bar, empty]
eight = [line, side_bars, line, side_bars, line]
nine = [line, side_bars, line, right_bar, line]
zero = [line, side_bars, empty, side_bars, line]

arr = [zero, one, two, three, four, five, six, seven, eight, nine]

num = list(map(int, list(str(num))))
numArr = list()

for n in num:
    numArr.append(arr[n])

test(numArr)