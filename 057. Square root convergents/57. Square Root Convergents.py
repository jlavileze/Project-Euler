from math import sqrt

def recurrence_numerator(n):
    y = 0.5 * ((1.0-sqrt(2))**(n+1)+(1.0+sqrt(2))**(n+1))
    return int(y)
    
def recurrence_denominator(n):
    y = 0.25*((sqrt(2)-2.0)*(-1*(1.0-sqrt(2))**n)+(2.0+sqrt(2))*(1.0+sqrt(2))**n)
    return int(y)
    

counter = 0

#for i in range(1000):
#    if len(str(recurrence_numerator(i))) > len(str(recurrence_denominator(i))):
#        counter += 1
        

#print counter

def convergents_counter(n):
    counter = 0
    iterant = 0
    num_1 = 1
    den_1 = 1
    num_2 = 3
    den_2 = 2
    while iterant < n:
        if len(str(num_2)) > len(str(den_2)):
            counter += 1
        num_temp = num_2
        den_temp = den_2
        num_2 = 2 * num_temp + num_1
        den_2 = 2 * den_temp + den_1
        num_1 = num_temp
        den_1 = den_temp
        iterant += 1
    return counter

print convergents_counter(1000)