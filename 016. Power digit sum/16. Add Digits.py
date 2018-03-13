def add_digits(x_str):
    total = 0
    for char in x_str:
        total = total + int(char)
    return total    

x = 2 ** 1000
print add_digits(str(x))