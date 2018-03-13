digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

def isPandigital(x):
    x_str = str(x)
    return all(char in x_str for char in digits)
    
    
results_list = []

for i in range(2000):
    for j in range(2000):
        concat = str(i)+str(j)+str(i*j)
        if isPandigital(concat) and len(concat) < 10:
            results_list.append(i*j)
            
results_list = set(results_list)

print results_list
print 5346+5796+6952+4396+7852+7632+7254