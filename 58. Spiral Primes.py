from math import sqrt, ceil

def lower_right(n):
    return (2*n-1) ** 2
    
def lower_left(n):
    return lower_right(n)-(2*n - 2)
    
def upper_left(n):
    return lower_left(n) - (2*n - 2)
    
def upper_right(n):
    return upper_left(n) - (2*n - 2)
    
def isPrime(x):
    for i in range(2, int(ceil(sqrt(x)))+1):
        if x % i == 0:
            return False
    else:
        return True

i=2
counter = 0

while True:
    if isPrime(lower_left(i)):
        counter += 1
    if isPrime(upper_left(i)):
        counter += 1
    if isPrime(upper_right(i)):
        counter += 1
    if float(counter)/(4.0*i-3.0) < 0.1:
        print sqrt(lower_right(i))
        break
    i += 1