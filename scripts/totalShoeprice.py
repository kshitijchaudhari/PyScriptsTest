from collections import Counter

def main():
    s, psizes, prices = getinputs()
    calctotal(s, psizes, prices)

def getinputs():
    n = int(input())
    sizes = Counter(input().split(" "))
    cnum = int(input())
    psize = []
    pprice= []
    j=0
    for j in range(cnum):
        m, n = input().split(" ")
        psize.append(m)
        pprice.append(n)
    return [sizes, psize, pprice]

def calctotal(s,ps,pp):
    total=0
    for a,b in enumerate(ps):
        if s[b]>0:
            s[b] = int(s[b])-1
            total = total + int(pp[a])
    print(total)


if __name__ == '__main__':
    main()
