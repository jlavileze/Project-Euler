def self_power(x):
    return x ** x
    
sum_nums = 0

for i in range(1,1001):
    sum_nums += self_power(i)
    
print (sum_nums % 10000000000)