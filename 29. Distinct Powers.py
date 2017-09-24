def powers(a,b):
    return a ** b
    
list_of_powers = []

for i in range(2,101):
    for j in range(2,101):
        list_of_powers.append(powers(i,j))
        
print len(set(list(list_of_powers)))