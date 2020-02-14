def wrapper(f):
    def phsort(v):
        if len(v) == 11:
            v= v[1:6] + v[6:]
        elif len(v) == 12:
            v = v[2:7] + v[7:]
        elif len(v) == 13:
            v = v[3:8] + v[8:]
        elif len(v) == 10:
            v = v[:5] + v[5:]
        return int(v)
    def fun(l):
        for i in l:
            if len(i)==11:
                return i[1:6] + i[6:]
            elif len(i)==12:
                return i[2:7] + i[7:]
            elif len(i)==13:
                return i[3:8] + i[8:]
            elif len(i)==10:
                return i[:5] + i[5:]
            else:
                print("Something's wrong")
    return fun


@wrapper
def sort_phone(m):
    print(*sorted(m), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)

