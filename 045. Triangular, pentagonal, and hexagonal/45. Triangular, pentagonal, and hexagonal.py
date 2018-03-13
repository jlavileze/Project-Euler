from math import sqrt

def isInt(x):
    if x - round(x) == 0:
        return True
    else:
        return False
    

def isTriangular(y):
    x = sqrt(2*y + 0.25) -0.5
    return isInt(x)

def isPentagonal(x):
    y = sqrt(2.0*x/3.0 + 1.0/36.0) + 1.0/6.0
    return isInt(y)
    
def isHexagonal(x):
    y = sqrt(x/2.0 + 1.0/16.0) + 0.25
    return isInt(y)
    
def nth_triangular(x):
    y = x*(x+1)/2
    return y
    
many_triangulars = []

for i in range(2,1000000):
    many_triangulars.append(nth_triangular(i))
    
for triangle in many_triangulars:
    if isPentagonal(triangle):
        if isHexagonal(triangle):
            print triangle
