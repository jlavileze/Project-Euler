from fractions import gcd


def lowest_terms(x,y):
    d = gcd(x,y)
    return (x/d,y/d)

def digit_cancelling(x,y):
    x_str = str(x)
    y_str = str(y)
    if x_str[0] == y_str[0]:
        return (int(x_str[1]),int(y_str[1]))
    elif x_str[0] == y_str[1]:
        return (int(x_str[1]),int(y_str[0]))
    elif x_str[1] == y_str[0]:
        return (int(x_str[0]),int(y_str[1]))
    elif x_str[1] == y_str[1]:
        return (int(x_str[0]),int(y_str[0]))
    else:
        return (0,0)

for i in range(10,100):
    for j in range(i+1,100):
        if lowest_terms(i,j) == digit_cancelling(i,j) and (i % 10 != 0 and j % 10 != 0):
            print (i,j)

print 
