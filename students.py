def secSort(val):
    return val[1]
def alpha(v):
    return v[0]

def students():
    s=[]
    p=int(input())
    for _ in range(p):
        name = input()
        score = float(input())
        s.append([name,score])
    print(s)
    s.sort(key=secSort)
    print(s)
    if (s[0][1] == s[1][1] and s[1][1]==s[2][1]):
        s.pop(0)
        s.pop(0)
        p=p-2
    elif (s[0][1] == s[1][1]):
        s.pop(0)
        p = p - 1
    i=1
    fl=[]
    sval=s[1][1]
    while i<p:
        if sval==s[i][1]:
            fl.append(s[i][0])
        i=i+1
    fl.sort(key=alpha)
    print(fl)
students()