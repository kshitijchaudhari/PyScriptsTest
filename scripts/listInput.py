if __name__ == '__main__':
    N = int(input())
    m = 1
    r = []
    for m in range(N):
        a = []
        a = input().split()
        if "insert" in a[0]:
            r.insert(int(a[1]), int(a[2]))
        elif "print" in a[0]:
            print(r)
        elif "remove" in a[0]:
            r.remove(int(a[1]))
        elif "append" in a[0]:
            r.append(int(a[1]))
        elif "sort" in a[0]:
            r.sort()
        elif "pop" in a[0]:
            r.pop()
        elif "reverse" in a[0]:
            r.reverse()
