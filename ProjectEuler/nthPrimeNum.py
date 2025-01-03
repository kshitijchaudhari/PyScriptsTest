# <p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.</p>
# <p>What is the $10\,001$st prime number?</p>

nth = 10001
primelist = []
maxNumRange = 100000000000

def getPrime():
    while (len(primelist)<nth):
        for _ in range(1, maxNumRange, 1):
            last_digit = int(str(_)[-1])
            checkPrime = True
            if(_==1 or _==2 or _==5):
                primelist.append(_)
                continue
            if(last_digit not in [0,2,4,5,6,8]):
                for e in range(2,_, 1):
                    if(_%e==0):
                        checkPrime = False
                        continue
                if(checkPrime):
                    primelist.append(_)
                    if(len(primelist)>nth):
                        break
    print(f'The {nth} prime number is {primelist[nth]}')

getPrime()