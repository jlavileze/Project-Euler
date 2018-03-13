def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def count_distinct_primes(x):
    return len(set(prime_factors(x)))

for i in range(100,1000000):
    if count_distinct_primes(i) == 4:
        if count_distinct_primes(i+1) == 4:
            if count_distinct_primes(i+2) == 4:
                if count_distinct_primes(i+3) == 4:
                    print i
                    break

