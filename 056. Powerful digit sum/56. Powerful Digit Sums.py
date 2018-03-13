def add_digits(x):
    x_str = str(x)
    total = 0
    for char in x_str:
        total = total + int(char)
    return total    


maximum_sum = 0

for i in range(100):
    for j in range(100):
        i_to_j = i ** j
        if add_digits(i_to_j) > maximum_sum:
            maximum_sum = add_digits(i_to_j)
            
print maximum_sum