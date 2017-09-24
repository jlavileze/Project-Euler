from fractions import gcd

def reduced_fraction(frac):
    hcf = gcd(frac[0],frac[1])
    return (frac[0]/hcf,frac[1]/hcf)

output = []

for i in range(2,1000001):
    for j in range(1,i):
        frac = reduced_fraction((j,i))
        output.append(frac)

len(set(output))