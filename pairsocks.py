def getsocks():
    # t = input("Input the total number of individual socks ")
    # socks = []
    pairCount = {}
    # extraSocks = []
    # for i in range(int(t) + 1):
    #     socks.append(input("enter sock id "))
    socks = ['9', '5', '8', '8', '5', '9','3', '3']
    socks.sort()
    print(socks)
    m = 0
    for s in socks:
        if m + 1 < len(socks):
            if s == socks[m + 1]:
                pairCount[s] = int(pairCount.get(s, "0")) + 1
                socks.pop(m)
                if m < len(socks):
                    socks.pop(m)
            else:
                continue
        m=m+1
    extraSocks = socks
    print("Extra socks are ", extraSocks)
    print("Pairs are ", pairCount)


getsocks()
