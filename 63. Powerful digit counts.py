def x_power_y(x,y):
    powers = str(x ** y)
    len_powers = len(powers)
    if len_powers == y:
        return True
    else:
        return False

counter = 0

for i in range(1,10):
    for j in range(1,10000):
        if x_power_y(j,i):
            counter += 10
            

print counter
    
