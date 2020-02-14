def runnerUp():
    n = int(input("Enter the total students "))
    A = input().split()
    x = 0
    for i in A:
        A[x] = int(A[x])
        x = x + 1
    fL = []
    for num in A:
        if num not in fL:
            fL.append(num)
    fL.sort(reverse=True)

    print(fL[1])

runnerUp()

