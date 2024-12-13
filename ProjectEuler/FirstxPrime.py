# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10,001st prime number?

nthPrime = 10
maxNum = 10000000
primelist = []

def sortPrime(arr):
    for _ in arr:
        isPrime = False
        last_digit = int(str(c)[-1])
        if(last_digit==0 or last_digit==2 or last_digit==4 or last_digit==6 or last_digit==8 or last_digit==5):
            isPrime = False
            continue
            for c in range(2,_-1):
                if(isPrime):
                    primelist.append(_)
                    if(len(primelist)>nthPrime):
                        print(f'The prime number list is {primelist}')
                        print(f'The {nthPrime}th prime number is {primelist[nthPrime]}')

sortPrime(range(1,maxNum))