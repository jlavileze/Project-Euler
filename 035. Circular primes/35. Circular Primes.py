import math
from itertools import permutations

def isPrime(x):
    if x == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(x)))+1):
        if x % i == 0:
            return False
    else:
        return True
        

primes_under_million = []

for i in range(8,10**6):
    if isPrime(i):
        primes_under_million.append(i)
        
adjusted_primes = [2, 3, 5, 7]

def exclude(word, char):
    for i in word:
        if i == char:
            return False
            break
    else:
        return True
        

def possible_primes(x):
    item_str = str(x)
    y = (exclude(item_str, str(0)) and exclude(item_str, str(2)) and exclude(item_str, str(4)) and exclude(item_str, str(5)) and exclude(item_str, str(6)) and exclude(item_str, str(8)))
    return y
    
for item in primes_under_million:
    item_str = str(item)
    if possible_primes(item):
       adjusted_primes.append(item)
    

def cycles(x):
    temp_var = str(x) + str(x)
    str_len = len(str(x))
    cycle_list = []
    for i in range(0,str_len):
        cycle_list.append(int(temp_var[i:i+str_len]))
    return cycle_list
    
circular_primes = []

for i in adjusted_primes:
    prime_cycles = cycles(i)
    for k in prime_cycles:
        if not isPrime(k):
            break
    else:
        circular_primes.append(i)
    
def sum_list(lonum):
    total = 0
    for i in lonum:
        total += i
    return total
    
print len(circular_primes)
    
    
    
    
    