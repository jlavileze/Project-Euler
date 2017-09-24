from math import ceil, sqrt

def isPrime(x):
    for i in range(2, int(ceil(sqrt(x)))+1):
        if x % i == 0:
            return False
    else:
        return True
        
list_primes = [2]

for i in range(2,1000):
    if isPrime(i):
        list_primes.append(i)
        

def isPrime_eff(x):
    for i in list_primes:
        if i >= x:
            return True
        elif x % i == 0:
            return False
    else:
        return True

def goldbach_fun(p,s):
    return p + 2 * (s**2)

goldbach_list = []

def isOdd(x):
    if x % 2 == 1:
        return True
    else:
        return False

for i in list_primes:
    for j in range(100):
        g = goldbach_fun(i,j)
        if isOdd(g):
            if not isPrime_eff(g):
                goldbach_list.append(g)

odds = []

for i in range(1,1000000):
    odds.append(2*i-1)

print set(goldbach_list)-set(odds)