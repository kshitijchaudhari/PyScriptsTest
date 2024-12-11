# A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.
# Find the largest palindrome made from the product of two $3$-digit numbers

import csv
import itertools

highnum = 999
lownum = 99
palinNum = 0
li = []
mux = []

def checkPalindrome(m,c1,c2):
    if int(m)==int(str(int(m))[::-1]):
        mux.append([c1,c2])
        li.append([m])
        #print(f'{li}')


def reductionPalindromeNumber(n1, n2):
    for x,y in itertools.product(range(n1, n2, -1), range(n1, n2, -1)):
        product = x*y
        checkPalindrome(product,x,y)
    print(f'The largest palindrome number is {max(li)}')
    gotoExit(li, mux)
        

def gotoExit(l, m): # exiting the program but writing to a csv file first
    t = 0
    writer = csv.writer(open("C:\\Users\\kshit\\Downloads\\test.csv", 'w'))
    for _ in l:
        t +=1
        writer.writerow(_)
    #exit()
    

reductionPalindromeNumber(highnum,lownum)