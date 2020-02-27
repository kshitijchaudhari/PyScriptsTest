
arr = []


def getpattern(size):
    a = [chr(x) for x in range(97, (97 + size))]
    pattern = "-".join(a)
    midline = pattern[::-1] + pattern[1::]
    linelength = len(midline)
    arr.append(midline)
    expandmidline(pattern, size)
    for i, j in enumerate(arr):
        print(arr[i])


def expandmidline(pat, size):
    x=1
    left = pat
    right = pat[1:]
    for b in range(1, size):
        left = left[2:]
        right = right[2:]
        pat = ("-" *x *2) + left[::-1] + right[:] + ("-" *x* 2)
        arr.insert(0, pat)
        arr.append(pat)
        x=x+1



getpattern(11)
