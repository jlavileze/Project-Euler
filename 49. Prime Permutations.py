from math import ceil, sqrt

def isPrime(x):
    for i in range(2, int(ceil(sqrt(x)))+1):
        if x % i == 0:
            return False
    else:
        return True
        
list_primes = []

for i in range(1000,10000):
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

def isArithProg(x,y,z):
    if z-y == y-x:
        return True
    else:
        return False

def isPerm(x,y):
    x_str = str(x)
    y_str = str(y)
    if sorted(x_str) == sorted(y_str):
        return True
    else:
        return False

for x in list_primes:
    for i in range(2,4001,2):
        if x + i + i > 9999:
            break
        elif isPrime(x+i) and isPrime(x+i+i):
            if isPerm(x,x+i) and isPerm(x,x+i+i):
                print str(x) + str(x+i) + str(x+i+i)


