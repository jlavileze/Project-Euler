from fractions import gcd
from math import ceil,sqrt

def gcd_euclidean(x,y):
    # x > y
    # buggy
   while x % y != 0:
       temp = x
       x = temp
       y = temp % y
   else:
       return y


def isOne(num):
    if num == 1:
        return True
    else:
        return False

## Possible solution, we could use a neater, more efficient
## computation of Euler's Totient Function. Phi(n) = n*sum_over_primes_dividing_n(1-1/p)
def euler_totient(n):
    counter = 0
    for i in range(1,n):
        if isOne(gcd(n, i)):
            counter += 1
            
    return counter
    
def n_over_phi(n):
    return n/float(euler_totient(n))
    
#maximum_ratio = 0
#max_arg = 2

#for n in range(2,1000001):
#    temp_ratio = n_over_phi(n)
#    if temp_ratio > maximum_ratio:
#        maximum_ratio = temp_ratio
#        max_arg = n
        
#print maximum_ratio
#print max_arg

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

euler_test_primes = [2]

for i in range(3,500000):
    if isPrime_eff(i):
        euler_test_primes.append(i)


def phi(n):
    n_temp = n
    product = 1
    for p in euler_test_primes:
        if n_temp % p == 0:
            product *= (1.0 - 1.0/p)
            n_temp = n_temp/p
        elif p > n/2 + 1:
            break
    return n * product
    
def n_over_phi_eff(n):
    return n/phi(n)


max_ratio = n_over_phi_eff(390390)
max_n = 390390

## Running it at the office. Max ratio until now occurs at 390390
## Loop must run for at least n = 500000 because n/phi(n) = 2n/phi(2n)


for n in range(500000,1000001):
    ratio = n_over_phi_eff(n)
    if ratio > max_ratio:
        max_ratio = ratio
        max_n = n
        print n

print "The answer is: "
print max_ratio
print max_n
    
