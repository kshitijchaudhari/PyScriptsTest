# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible with no remainder by all of the numbers from 1 to 20

maxnum = 500000000
li = list(range(1,21))

def getLowestMultiple(m):
    for _ in range(1,m):
        last_char = int(str(_)[-1])
        #print(f'Last character for number {_} is {last_char}')
        if (last_char==0):
            if(all(_%x==0 for x in li)):
                print(f'The smallest positive number evenly divisible by 1 to 20 is {_}')
                exit()

getLowestMultiple(maxnum)
            