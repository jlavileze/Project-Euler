def isInt(x):
    if x-round(x) == 0:
        return True
    else:
        return False

def pythagoras(x,y):
    z = sqrt(x**2 + y**2)
    return z
    
def isTriple(x,y):
    return isInt(pythagoras(x,y))

solution_keys = {}

for key in range(1,1001):
    solution_keys[key] = 0
    
for i in range(3,500):
    for j in range(3,500):
        k = pythagoras(i,j)
        perimetre = int(i + j + k)
        if perimetre > 1000:
            break
        elif isTriple(i,j):
            solution_keys[perimetre] += 1

max_key = 0
max_sol = 0

#for key in solution_keys:
#    if solution_keys[key] > max_sol:
#        max_key = key

print solution_keys
