from math import ceil, sqrt


def nth_triangular_number(n):
    return (n*(n+1))/2
    
def list_factors(n):
    factors = []
    for i in range(1,int(n+1)):
        if n % i == 0:
            factors.append(i)
            
    return factors

def number_of_factors(num):
    return len(list_factors(num))
    
def num_fact_eff(x):
    num_factors = 0
    for i in range(1,int(ceil(sqrt(x)))):
        if x % i == 0:
            num_factors += 2
    return num_factors



i = 1800
while True:
    tri_num = nth_triangular_number(i)
    num_fact = num_fact_eff(tri_num)
    print "i=" + str(i) + ", ",
    print "x=" + str(tri_num) + ", ",
    print num_fact
    if num_fact > 500:
        break
    i += 1
