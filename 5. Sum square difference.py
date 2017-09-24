def square_sum_first_n(x):
    sum_of_x = (x * (x+1))/2
    square_sum = sum_of_x ** 2
    return square_sum

def sum_of_squares(x):
    sum_squares = (x * (x+1) * (2 * x + 1)) / 6
    return sum_squares
    
def sum_square_dif(x):
    return abs(sum_of_squares(x) - square_sum_first_n(x))
    
print sum_square_dif(100)
    