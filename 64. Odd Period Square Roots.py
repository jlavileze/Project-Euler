from math import sqrt, floor


def continued_fraction(seed, residue_array, coefficient_array):
    if sqrt(seed) - floor(sqrt(seed)) == 0:
        return 0
    
    coefficient = int(floor(seed))
    residue = 1.0/(seed - coefficient)
    coefficient_array.append(coefficient)    
    
    for res in residue_array:
        if abs(residue-res) < 0.000001:
            return coefficient_array
    else:
        residue_array.append(residue)

        return continued_fraction(residue, residue_array, coefficient_array)


def problem64(x):
    return continued_fraction(sqrt(x),[],[])


for i in range(2,14):
    problem64(i)