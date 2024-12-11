#  The prime factors of $13195$ are $5, 7, 13$ and $29$.
#  What is the largest prime factor of the number $600851475143$
import time

st = time.perf_counter()
num = 600851475143
factors = []
primefactors = []

def largestPrime(n):
    for _ in range(1,n):
        if (n%_==0):
            factors.append(_)
    print(f'The factors for {n} are {factors}')

def sortPrimeFactors(arr):
    for _ in arr:
        isPrime = True
        for c in range(2,_-1):
           last_digit = int(str(c)[-1])
           if(c==0 or c==2 or c==4 or c==6 or c==8 or c==5 or _%c==0):
                isPrime = False
        if(isPrime):
            primefactors.append(_)
    print(f'The prime factor are {primefactors}')
    print(f'Larget prime factor is {primefactors[len(primefactors)-1]}')

largestPrime(num)
sortPrimeFactors(factors)
print(f'Total time for processing: {time.perf_counter() - st}')