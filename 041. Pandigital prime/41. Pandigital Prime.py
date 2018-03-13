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
        

def is_pandigital(nr, n):
    nr = str(nr)
    beg=nr[0:n]
    end=nr[-n:]
    for i in map(str, range(1, n + 1)):
        if i not in beg or i not in end:
            return False
    return True
    
max_prime = 0



for i in range(10**6,10**7):
    if is_pandigital(i,7):
        if isPrime_eff(i):
            print i
            max_prime = i
            
print "Max prime is: " + str(max_prime)
            
