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


def quadratic_polynomial(x,a,b,c):
    return (a * x ** 2) + (b * x) + c
    
    
def discriminant(a,b,c):
    return b**2 - 4 * a * c
    
# We look for polynomials which have a discriminant of -163, as these produce long sequences of primes    
specific_disc = []

for i in range(-1000,1000):
    for j in range(-1001,1001):
        if discriminant(1,i,j) == -163:
            index = [i,j]
            specific_disc.append(index)
        

def prob_poly(x,locoeff):
    a = locoeff[0]
    b = locoeff[1]
    y = x ** 2 + a * x + b
    return y

max_prime_count = 0
max_prime_prod = 0

for coeffs in specific_disc:
    counter = 0
    for x in range(200):
        if isPrime_eff(prob_poly(x,coeffs)):
            counter += 1
        else:
            if counter > max_prime_count:
                max_prime_count = counter
                max_prime_prod = coeffs[0] * coeffs[1]
            break
        

print max_prime_prod