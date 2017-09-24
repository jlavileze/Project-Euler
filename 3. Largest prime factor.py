import math

factors = []

def list_factors(n):
    for i in range(1,n+1):
        if n % i == 0:
            factors.append(i)
            
    print factors
    
def isPrime(x):
    for i in range(2, int(math.ceil(math.sqrt(x)))+1):
        if x % i == 0:
            return False
    else:
        return True
        
prime_factors = []

def list_prime_factors(n):
    if n % 2 == 0:
        prime_factors.append(2)
    for i in range(2, int(math.ceil(math.sqrt(n)))):
        if isPrime(i) and n % i == 0:
            prime_factors.append(i)
            
    print prime_factors
