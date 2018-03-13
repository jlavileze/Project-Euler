from math import sqrt


def isInt(x):
    if x - round(x) > 0:
        return False
    else:
        return True

def nth_root(N,k):
    """Return greatest integer x such that x**k <= N"""
    x = int(N**(1/k))      
    while (x+1)**k <= N:
        x += 1
    while x**k > N:
        x -= 1
    return x
    
def iroot(k, n):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s
    
total = 0

for i in range(1,10):
    if isInt(i):
        total += 1
        

for i in range(10,100):
    if isInt(sqrt(float(i))):
        total += 1
        
print total
