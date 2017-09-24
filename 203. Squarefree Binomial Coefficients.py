from math import factorial

def ncr(n, r):
    return (factorial(n)/(factorial(r)*factorial(n-r))

primes = [2,3,5,7,11]
sqr_primes = [x**2 for x in primes]



def isSquareFree(x):
    for i in sqr_primes:
        if x % i == 0:
            return False
    
    return True
    
sqr_free_coefs = [1]

for n in range(2,9):
    for r in range(0,n+1):
        bin_coef = ncr(n,r)
        if isSquareFree(bin_coef):
            # print str(n) + "C" + str(r) + " = " + str(bin_coef)
            sqr_free_coefs.append(bin_coef)

total = 0

set_sqr_free = set(sqr_free_coefs)

for i in set_sqr_free:
    total += i 

print total

