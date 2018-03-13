from math import factorial, ceil, sqrt

def s_of_p(p):
    total = 0
    for i in range(1,6):
        total += factorial(p-i)
    return total % p
    
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

many_primes = []

for i in range(5,100000000):
    if isPrime_eff(i):
        many_primes.append(i)
        
answer = 0
for prime in many_primes:
    print prime
    answer += s_of_p(prime)

print "The answer is:"    
print answer