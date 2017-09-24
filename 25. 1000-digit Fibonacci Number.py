def nth_fibonacci(n):
    # for n >= 3
    counter = 2
    f_n = 1
    f_n1 = 1
    f_n2 = 0
    while counter < n:
        f_n2 = f_n + f_n1
        f_n = f_n1
        f_n1 = f_n2
        counter += 1
    return f_n2
    
def fib_digits(x):
    fib_length = len(str(nth_fibonacci(x)))
    return fib_length
    
print fib_digits(1000)
    
for i in range(10000000):
    if fib_digits(i) == 1000:
        print i
        break