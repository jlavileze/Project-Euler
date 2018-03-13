digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def is_pandigital(nr, n):
    nr = str(nr)
    beg=nr[0:n]
    end=nr[-n:]
    for i in map(str, range(1, n + 1)):
        if i not in beg or i not in end:
            return False
    return True
    
def concat_product(x,listupto):
    output_str = ""
    lonum = []
    for j in range(1, listupto+1):
        lonum.append(j)
    for i in lonum:
        output_str = output_str + str(x*i)
    return int(output_str)
    
maximum_product = 0

for i in range(100000):
    for j in range(1,5):
        prod = concat_product(i,j)
        if prod > 999999999:
            break
        elif prod > maximum_product:
            if is_pandigital(prod,9):
                maximum_product = prod

print maximum_product