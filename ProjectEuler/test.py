# test file to run and check some code for larger programs

import itertools

a = 100
b = 10
c = 0

def testcode():
    i = 0
    for m,n in itertools.product(range(25, 15, -1), range(17, 15, -1)):
        print(f'The current iteration is {i}')
        print(f'values of m and n are {m} and {n}')
        i +=1     
    

def testcode2():
    m = "testcoden"
    n = 3463644
    print(f'Last character of string is {m[-1]}')
    print(f'Last character of number is {str(n)[-1]}')


testcode2()