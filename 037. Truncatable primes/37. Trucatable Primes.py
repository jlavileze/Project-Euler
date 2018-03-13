def isPrime(x):
    if x<2:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.ceil(math.sqrt(x)))+1):
        if x % i == 0:
            return False
    else:
        return True
        

primes_test_list = []

for i in range(10**5):
    if isPrime(i):
        primes_test_list.append(i)
        

def isPrime_eff(x):
    if x < 2:
        return False
    for i in primes_test_list:
        if x == i:
            return True
        if x % i == 0:
            return False
    else:
        return True
        
        
        

def left_truncate(x):
    x_str = str(x)
    list_of_numbers = []
    num_digits = len(x_str)
    for i in range(num_digits):
        list_of_numbers.append(int(x_str[i: num_digits]))
        
    return list_of_numbers
    
def right_truncate(y):
    y_str = str(y)
    list_of_numbers = []
    num_digits = len(y_str)
    for i in range(num_digits, 0, -1):
        list_of_numbers.append(int(y_str[0: i]))
    return list_of_numbers
    

primes_under_million = []

for i in range(8,10**6):
    if isPrime_eff(i):
        primes_under_million.append(i)


truncatable_primes = []

for item in primes_under_million:
    candidate_primes_1 = right_truncate(item)
    for candidates_1 in candidate_primes_1:
        if not isPrime_eff(candidates_1):
            break
    else:
        candidate_primes_2 = left_truncate(item)
        for candidates_2 in candidate_primes_2:
            if not isPrime_eff(candidates_2):
                break
        else:
            truncatable_primes.append(item)
            
print truncatable_primes

## Possible solution: Make list of primes, remove those who contain 0, 2, 4, 5, 6, 8 in 
## their decimal representation 

