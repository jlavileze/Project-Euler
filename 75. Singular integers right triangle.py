def euclid_formula(m,n,k):
    a = m ** 2 - n ** 2
    b = 2*m*n
    c = m ** 2 + n ** 2
    return (k*a,k*b,k*c)

def perimeter(lengths):
    return lengths[0]+lengths[1]+lengths[2]

perimeters = {}

for m in range(2,5000):
    for n in range(1,m):
        for k in range(1,125001):
            triangle = euclid_formula(m,n,k)
            per = perimeter(triangle)
            if per > 1500000:
                break
            else:
                

