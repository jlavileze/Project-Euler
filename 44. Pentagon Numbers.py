from math import sqrt

def nth_pentagonal(n):
    return n * (3*n-1)/2
    

def isInt(x):
    if x - round(x) == 0:
        return True
    else:
        return False
    
    
def isPentagonal(x):
    y = sqrt(2.0*x/3.0 + 1.0/36.0) + 1.0/6.0
    return isInt(y)
    
many_pentagonals = []

for i in range(1,10000):
    many_pentagonals.append(nth_pentagonal(i))
    
total_pent = len(many_pentagonals)

candidates = []

for count, item in enumerate(many_pentagonals):
    for j in range(count, total_pent):
        pent_diff = many_pentagonals[j] - item
        if isPentagonal(pent_diff):
            pent_sum = many_pentagonals[j] + item
            if isPentagonal(pent_sum):
                cand = [item,many_pentagonals[j]]
                candidates.append(cand)
                
                
print candidates
print abs(1560090-7042750)