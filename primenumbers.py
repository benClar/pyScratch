import math

def get_primes(limit):
    return filter(lambda n: isPrime(n), range(2,limit+1))

def isPrime(n):
    for i in range(2,int(math.sqrt(n))):
        if not n%i:
            return False
    return True

print get_primes(100)