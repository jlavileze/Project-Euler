def list_proper_divisors(x):
    proper_divisors = []
    for i in range(1,x):
        if x % i == 0:
            proper_divisors.append(i)
    return proper_divisors
    
def sum_divisors(x):
    list_divisors = list_proper_divisors(x)
    total = 0
    for i in list_divisors:
        total = total + i
    return total
    

def isAbundant(x):
    if x >= sum_divisors(x):
        return False
    if x < sum_divisors(x):
        return True
        

upper_limit = 28123

abundant_numbers = []

for i in range(1,14100):
    if isAbundant(i):
        abundant_numbers.append(i)
        
#sum_abundant_nums = []
#list_of_nums = [] 
#for i in abundant_numbers:
#    for j in range(i, upper_limit):
#        sum_abundant_nums.append(i+j)

#for i in range(upper_limit+1):
#    list_of_nums.append(i)

def sum_list(x):
    total = 0
    for i in x:
        total = total + i
        
    return total

#print sum_abundant_nums

sum_of_abundant = []
len_abun = len(abundant_numbers)


for count, elem in enumerate(abundant_numbers):
    for j in range(count, len_abun-1):
        x = elem + abundant_numbers[j]
        sum_of_abundant.append(x)
        
list_of_nums = []

for i in range(28124):
    list_of_nums.append(i)
    
total_abundant = sum_list(set(list_of_nums)-set(sum_of_abundant))
    

print total_abundant