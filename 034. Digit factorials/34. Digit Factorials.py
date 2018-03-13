from math import factorial

def digit_factorial(x):
    x_str = str(x)
    total = 0
    for char in x_str:
        total += factorial(int(char))
    return total
    
def check_equality(x):
    if x == digit_factorial(x):
        return True
    else:
        return False
        
total_fact = 0

for i in range(4,10**7):
    if check_equality(i):
        total_fact += i
        
print total_fact
    