def finaList():
    X= int(input("First variable "))
    Y= int(input("second variable "))
    Z= int(input("Third variable "))
    N= int(input('Sum variable '))
    i=0
    j=0
    k=0
    fL = []
    for i in range(X+1):
        for j in range(Y+1):
            for k in range(Z+1):
                if (i+j+k)!=N:
                    fL.append([i,j,k])
                else:
                    pass
    print(fL)

finaList()
