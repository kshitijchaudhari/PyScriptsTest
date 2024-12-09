# If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
# Find the sum of all the multiples of $3$ or $5$ below $1000$.

num = 1000
multiples = []

def multiplesOf3(n):
    print(f'Finding the multiples of {n}')
    for _ in range(n):
        if(_%3 ==0 or _%5==0):
            multiples.append(_)
            print(f'Added {_} since it is multiple of 3 or 5')
    print(f'The sum of all multiples of 3 and 5 from 0 to {n} is {sum(multiples)}')
   

multiplesOf3(num)