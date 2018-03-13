from math import sqrt,ceil
from collections import OrderedDict

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
        

many_primes = [2]

for i in range(3,3932):
    if isPrime_eff(i):
        many_primes.append(i)

cumulative = 0
cumulative_dist = OrderedDict()
for prime in many_primes:
    cumulative += prime
    cumulative_dist[prime] = cumulative


cum_max = 997661

for i in many_primes:
    cum_max -= i 
    if isPrime_eff(cum_max):
        print cum_max
        break
