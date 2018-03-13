def coefficients(n):
    if n == 0:
        return 2
    elif n % 3 == 0 or n % 3 == 1:
        return 1
    else:
        return 2 * (n+1) / 3

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
    
def convergents_recurrence(n):
    counter = 0
    p_n = 0
    p_n1 = 1
    p_n2 = 0
    q_n = 1
    q_n1 = 0
    q_n2 = 0
    while counter < n:
        p_n2 = coefficients(counter) * p_n1 + p_n
        q_n2 = coefficients(counter) * q_n1 + q_n
        p_n = p_n1
        q_n = q_n1
        p_n1 = p_n2
        q_n1 = q_n2
        counter += 1
    return (p_n2,q_n2)

convergents_recurrence(100)
total = 0
for char in '6963524437876961749120273824619538346438023188214475670667':
    total += int(char)

print total
    
