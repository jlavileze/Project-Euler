from math import factorial

def digit_factorial(x):
    total = 0
    for char in str(x):
        total = total + factorial(int(char))
        
def check_equality(x):
    if x == digit_factorial(x):
        return True
    else:
        return False
        
        
