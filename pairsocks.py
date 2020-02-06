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
    while(1):
        try:
            i = socks.index(socks[m],m+1)
            pairCount[socks[m]] = pairCount.get(socks[m],0) + 1
            socks.pop(i)
            socks.pop(m)

        except ValueError:
            pass

    extraSocks = socks
    print("Extra socks are ", extraSocks)
    print("Pairs are ", pairCount)


getsocks()
