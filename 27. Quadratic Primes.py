import math

def polynomial(n, a, b):
    y = n ** 2 + a * n + b
    return y

def isPrime(x):
    for i in range(2, int(math.ceil(math.sqrt(x)))+1):
        if x % i == 0:
            return False
    else:
        return True

def test_polynomials_in_range(x):
    largest_product = 1
    prime_count = 0
    max_prime = 0
    k = 0
    for i in range(-x-1,x+1):
        for j in range(-x-1,x+1):
            while isPrime(polynomial(k, i, j)):
                prime_count += 1
                if prime_count > max_prime:
                    max_prime = prime_count
                    largest_product = i * j
            else:
                k = 0
                prime_count = 0
                
    return largest_product
    
print test_polynomials_in_range(10)
                