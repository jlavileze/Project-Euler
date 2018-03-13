import time
start_time = time.time()

def n_reverse(n):
    n_str = str(n)
    n_reverse = n_str[::-1]
    return n + int(n_reverse)

def odd_digits(x):
    x_str = str(x)
    output = True
    for char in x_str:
        if int(char) % 2 == 0:
            output = False
            break
    return output

if odd_digits(n_reverse(409)):
    print 'true'
    
