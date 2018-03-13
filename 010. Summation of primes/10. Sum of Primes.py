def isPrime(x):
    if x == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(x)))+1):
        if x % i == 0:
            return False
    else:
        return True
        
def sum_of_primes_upto(x):
    total = 0
    for i in range(x+1):
        