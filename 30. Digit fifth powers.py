def fifth_power_of_digs(x):
    sum_powers = 0
    for c in str(x):
        sum_powers = sum_powers + int(c) ** 5
        
    return sum_powers
    


def check_equality(x):
    if x == fifth_power_of_digs(x):
        return True
    else:
        return False
        
sum_of_numbers = 0

for i in range(2,10**7):
    if check_equality(i):
        sum_of_numbers = sum_of_numbers + i
        
        
print sum_of_numbers