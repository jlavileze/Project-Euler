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


def is_pandigital(nr, n):
    nr = str(nr)
    beg=nr[0:n]
    end=nr[-n:]
    for i in map(str, range(1, n + 1)):
        if i not in beg or i not in end:
            return False
    return True

for k in range(100000,999999):
    fib_k = str(nth_fibonacci(k))
    digs = len(fib_k)
    if is_pandigital(fib_k[0:9],9):
        if is_pandigital(fib_k[digs-9:digs],9):
            print k
            break

