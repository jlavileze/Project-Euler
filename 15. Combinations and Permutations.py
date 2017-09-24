from math import factorial

def comb(n,r):
    return factorial(n)/((factorial(n-r))*factorial(r))
    
def perm(n,r):
    return factorial(n)/factorial(n-r)
    
print comb(40,20)