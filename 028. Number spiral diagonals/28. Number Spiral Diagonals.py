total = 1
for i in range(2,502):
    lead = (2*i - 1) ** 2
    difference = 2 * i - 2
    sum_step = lead * 4 - difference*6
    total += sum_step
    
print total