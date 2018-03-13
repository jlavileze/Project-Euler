from math import sqrt

## Diophantine equation is x^2 - Dy^2 = 1

def quad_diophantine(x,y,d):
    return (x ** 2) - (d * (y ** 2))
    
def isOne(num):
    if num == 1:
        return True
    else:
        return False


minimal_solution_set = {}

def diop_ret_x(d, y):
    return sqrt(1.0 + d * y ** 2.0)
    
def isInt(x):
    if x - round(x) == 0:
        return True
    else:
        return False

def isSquare(x):
    if isInt(sqrt(x)):
        return True
    else:
        return False

non_square_num = []

for i in range(2,1001):
    if not isSquare(i):
        non_square_num.append(i)
        


for d in non_square_num:
    for y in range(2,4000000):
        if isInt(diop_ret_x(d,y)):
            minimal_solution_set[d] = diop_ret_x(d,y)
            break
        
max_sol = 0
max_arg = 0

for key in minimal_solution_set:
    if minimal_solution_set[key] > max_sol:
        max_sol = minimal_solution_set[key]
        max_arg = key
        
## The code works, but the solution to the problem requires y taking incredibly large
## values. Research into implementing Pell's equation is required

print max_sol
print max_arg
