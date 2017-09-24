from math import factorial

def add_digits(x_str):
    total = 0
    for char in x_str:
        total = total + int(char)
    return total  
    
print add_digits(str(factorial(100)))