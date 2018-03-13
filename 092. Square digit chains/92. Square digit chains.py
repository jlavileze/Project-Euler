def square_digit_sum(x):
    x_str = str(x)
    x_out = 0
    for c in x_str:
        x_out += (int(c) ** 2)
    return x_out

def square_digit_end(x):
    if x == 1 or x == 89:
        return x
    else:
        return square_digit_end(square_digit_sum(x))

counter = 0

for i in range(1,10**7):
    if square_digit_end(i) == 89:
        counter += 1
        

print "Counter is:"
print counter