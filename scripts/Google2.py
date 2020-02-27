def solution(x,y):
    a=[-1,-1]
    c=list(x)
    for keyi,i in enumerate(c):
        for keyj,j in enumerate(c):
            if sum(x[keyi:keyj+1]) == y:
                return [keyi, keyj]
    print(a)


solution([1, 2, 3, 4], 15)
solution([4, 3, 10, 2, 8], 12)
solution([4, 3, 10, 2, 8], 14)
