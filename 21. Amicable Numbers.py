def list_proper_divisors(x):
    proper_divisors = []
    for i in range(1,x):
        if x % i == 0:
            proper_divisors.append(i)
    return proper_divisors
    
def sum_divisors(x):
    return sum(list_proper_divisors(x))
    
def are_amicable(x,y):
    if sum_divisors(x) == y and sum_divisors(y) == x:
        return True
    else:
        return False
        

association_list = {}

for i in range(1,10000):
    association_list[i] = sum_divisors(i)
    
total_amicable = 0

for key_i in association_list:
    for key_j in range(key_i+1,10000):
        if key_i == association_list[key_j] and key_j == association_list[key_i]:
            print str(key_i) + "  " + str(association_list[key_j]),
            print str(key_j) + "  " + str(association_list[key_i])
            total_amicable == total_amicable + key_j + key_i
            
            
print 220+284+1184+1210+2620+2924+5020+5564+6232+6368      