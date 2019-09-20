import bisect
st = set()


def make_str(s):
    global st
    if len(s) != 0:
        st.add(int(s))
    if len(s) == 6:
        return
    make_str(s + '4')
    make_str(s + '7')


make_str('')
arr = sorted(list(st))
idx = bisect.bisect(arr, int(input()))
print(arr[idx-1])