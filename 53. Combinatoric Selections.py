from math import factorial

def comb(n,r):
    return factorial(n)/((factorial(n-r))*factorial(r))

total = 0

for i in range(101):
    for j in range(0,i):
        if comb(i,j) > 10 ** 6:
            total += 1
            
print total