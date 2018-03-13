from math import factorial


def digit_factorial(number):
    num_str = str(number)
    total = 0
    for char in num_str:
        total += factorial(int(char))
    return total

def factorial_chain_length(seed,lonums):
    seed_fact = digit_factorial(seed)
    if seed_fact in lonums:
        return len(lonums)
    else:
        lonums.append(seed_fact)
        return factorial_chain_length(seed_fact,lonums)


def solution_fun(x):
    return factorial_chain_length(x,[x])

counter = 0

for i in range(1,1000000):
    if solution_fun(i) == 60:
        counter += 1

print counter