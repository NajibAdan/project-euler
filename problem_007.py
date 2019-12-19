# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
# we can see that the 6th prime is 13.

# What is the 10 001st prime number?
import math
results = [2,3]

def sieve(limit):
    sieve_list = [False for x in range(limit+1)]
    for x in range(1,int(math.sqrt(limit))+1):
        for y in range(1,int(math.sqrt(limit)+1)):
            n = 4 * x ** 2 + y ** 2
            if n<=limit and (n%12 == 1 or n%12==5): sieve_list[n] = not sieve_list[n]
            n = 3 * x ** 2 + y ** 2
            if n<=limit and n%12==7: sieve_list[n] = not sieve_list[n]
            n = 3 * x ** 2 - y ** 2
            if x>y and n<=limit and n%12==11: sieve_list[n] = not sieve_list[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve_list[x]:
            for y in range(x**2,limit+1,x**2):
                sieve_list[y] = False
    for p in range(5,limit):
        if sieve_list[p]: 
            results.append(p)

sieve(140000)
print(len(results))
print(results[10000])


def isPrime(n):
    if n==1:
        return False
    elif n<4:
        return True
    elif n %  2 ==0:
        return False
    elif n<9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f<=r:
            if n % f == 0:
                return False
            if n % (f+2) == 0:
                return False
            f = f+6
    return True

limit = 10001
count = 1
candidate = 1
while count != limit:
    candidate = candidate +2
    if isPrime(candidate):
        count += 1
    
print(candidate)